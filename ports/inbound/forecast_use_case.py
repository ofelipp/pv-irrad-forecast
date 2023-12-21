# ! ./venv/bin/python3.10

from abc import ABCMeta, abstractmethod

from domain.data import Data


class ForecastUseCase:
    __metadata__ = ABCMeta

    @abstractmethod
    def predict(self, features: Data) -> Data:
        raise NotImplementedError()
