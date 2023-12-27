# ! ./venv/bin/python3.10

from abc import ABCMeta, abstractmethod

from domain.data import Features


class PollerUseCase:
    __metadata__ = ABCMeta

    @abstractmethod
    def get_job(self, queue_name: str) -> list[Features]:
        """Return the first job arrived (FIFO)"""
        raise NotImplementedError()

    @abstractmethod
    def have_job(self, queue_name: str) -> bool:
        """Return if there is job to be processed"""
        raise NotImplementedError()

    @abstractmethod
    def process_job(self, job: dict) -> list[Features]:
        """Transform the job into domain features to the ML inference"""
        raise NotImplementedError()
