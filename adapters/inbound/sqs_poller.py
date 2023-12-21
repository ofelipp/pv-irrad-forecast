# ! ./venv/bin/python3.10

import numpy as np

from domain.data import Data
from ports.inbound.poller import Poller

TEST_MESSAGES = [
    Data(np.array([0, 0, 0]), "job_ulid", "message_from_queue"),
    Data(np.array([0, 0, 1]), "job_ulid", "message_from_queue"),
    Data(np.array([0, 1, 0]), "job_ulid", "message_from_queue"),
    Data(np.array([0, 1, 1]), "job_ulid", "message_from_queue"),
    Data(np.array([1, 0, 0]), "job_ulid", "message_from_queue"),
]


class SQSPoller(Poller):
    """SQS Poller: get job from SQS and transform into Data to Forecast"""

    def __init__(self):
        # self.__client = boto3.client("sqs")
        # self.queues = {"queue_name": "queue_url"}
        self.__messages = TEST_MESSAGES

    def get_job(self, queue_name: str) -> Data:
        return self.__messages.pop()

    def have_job(self, queue_name: str) -> bool:
        return len(self.__messages) > 0
