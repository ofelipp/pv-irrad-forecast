# ! ./venv/bin/python3.10

from abc import ABC, abstractmethod

import boto3
import os
from pathlib import Path
import pickle
import re

from domain.model import Model


def clean_key_name(key: str) -> str:
    return re.sub(r"^\w*/|\.mdl", "", str(key))\
        .replace("_", "")\
        .replace("/", ".")


class LoaderModelsInterface(ABC):
    """Load models for service forecast"""

    @abstractmethod
    def load_models(self, path: str) -> dict[str: Model]:
        raise NotImplementedError()


class LoaderModels(LoaderModelsInterface):
    """
    Load models directly from a directory, recursively, for service forecast
    """

    def load_models(self, path: str) -> dict[str: Model]:
        return {
            clean_key_name(model_path): pickle.load(model_path)
            for model_path in self.__search_models_paths(path)
        }

    @staticmethod
    def __search_models_paths(path: str) -> list:
        return list(Path(path).rglob("*.mdl"))


class S3LoaderModels(LoaderModelsInterface):
    """
    Load models directly from a S3 Bucket directory, recursively, for service forecast
    """

    def __init__(self, bucket: str):
        self.__client = boto3.client("s3")
        self.bucket = bucket

    def load_models(self, path: str) -> dict[str: Model]:
        return {
            clean_key_name(model_path): self.load_single_model(model_path)
            for model_path in self.__search_models_paths(path)
        }

    def load_single_model(self, path: str) -> callable:
        return pickle.loads(
            self.__client.get_object(Bucket=self.bucket, Key=path)["Body"].read()
        )

    def __search_models_paths(self, path: str) -> list:
        objects_list = self.__client.list_objects_v2(
            Bucket=self.bucket, Prefix=path
        )["Contents"]

        return [obj["Key"] for obj in objects_list if obj["Size"] != 0]
