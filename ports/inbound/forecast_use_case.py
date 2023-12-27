# ! ./venv/bin/python3.10

from abc import ABCMeta, abstractmethod

from domain.data import Features, Forecast


class ForecastUseCase:
    __metadata__ = ABCMeta

    @abstractmethod
    def predict(self, features: list[Features]) -> Forecast:
        raise NotImplementedError()
