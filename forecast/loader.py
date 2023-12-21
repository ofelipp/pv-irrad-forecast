# ! ./venv/bin/python3.10

from abc import ABC, abstractmethod

from pathlib import Path
import re

from domain.model import Model


def clean_key_name(key: str) -> str:
    return re.sub(r"^\w*/|\.pickle", "", str(key))\
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
            # TODO: import correctly the model
            clean_key_name(model_path): model_path.stem
            for model_path in self.__search_models(path)
        }

    @staticmethod
    def __search_models(path: str) -> list:
        return list(Path(path).rglob("*.pickle"))
