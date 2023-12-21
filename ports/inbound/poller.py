# ! ./venv/bin/python3.10

from abc import ABCMeta, abstractmethod

from domain.data import Data


class Poller:
    __metadata__ = ABCMeta

    @abstractmethod
    def get_job(self, queue_name: str) -> Data:
        raise NotImplementedError()

    @abstractmethod
    def have_job(self, queue_name: str) -> Data:
        raise NotImplementedError()
