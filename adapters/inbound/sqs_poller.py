# ! ./venv/bin/python3.10
import json
import os

import numpy as np

from domain.data import Features, ORDER_FEATURES
from domain.coordinates import Coordinates
from domain.station import Station
from ports.inbound.poller_use_case import PollerUseCase

with open("job_schema.json", "rb") as json_file:
    TEST_MESSAGES = json.load(json_file)


class SQSPoller(PollerUseCase):
    """SQS Poller: get job from SQS and transform into Data to Forecast"""

    def __init__(self):
        # self.__client = boto3.client("sqs")
        # self.queues = {"queue_name": "queue_url"}
        self.__messages = [TEST_MESSAGES]

    def get_job(self, queue_name: str) -> list[Features]:
        """Return the first job arrived (FIFO)"""
        return self.process_job(job=self.__messages.pop())

    def have_job(self, queue_name: str) -> bool:
        """Return if there is job to be processed"""
        return len(self.__messages) > 0

    def process_job(self, job: dict) -> list[Features]:
        """Transform the job into domain features to the ML inference"""
        coordinates = Coordinates(
            latitude=job["coordinates"]["latitude"],
            longitude=job["coordinates"]["longitude"]
        )

        station = Station(name=job["station"], coordinates=coordinates)

        return [
            Features(
                data=self.__get_features_data(hour_job),
                name=f"Features from {station.name} for predict " +
                     f"hour {hour_job['hour']}",
                station=station,
                hour=hour_job["hour"],
                features_names=ORDER_FEATURES
            )
            for hour_job in job["data"]
        ]

    def __get_features_data(self, item) -> np.array:
        return np.array([
            item[feature] if feature in item else None
            for feature in ORDER_FEATURES
        ])
