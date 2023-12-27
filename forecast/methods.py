from abc import ABC, abstractmethod
from dataclasses import dataclass, field

import numpy as np

from domain.data import Features, Forecast
from domain.model import Model


@dataclass
class ForecastMethod(ABC):
    """Basic Representation for a forecast method used in Service"""
    models: dict[str:Model] = field(default_factory=dict)

    @abstractmethod
    def predict_station(self, station_features: list[Features]) -> Forecast:
        """Predict the irradiance for entire Station"""
        raise NotImplementedError()

    @abstractmethod
    def predict_hour(self, hour_features: Features) -> Forecast:
        """Predict the irradiance for a specific hour and station"""
        raise NotImplementedError()

    @abstractmethod
    def set_models(self, models: dict[str:Model]):
        raise NotImplementedError()


@dataclass
class ForecastMappedStation(ForecastMethod):
    """Type of forecast designated to MAPPED Stations"""

    def predict_station(self, station_features: list[Features]) -> Forecast:
        """Predict the irradiance for entire Station"""

        forecast_results = {
            hour_feature.hour: self.predict_hour(hour_features=hour_feature)
            for hour_feature in station_features
        }

        print(forecast_results)

        return Forecast(
            data=forecast_results,
            station=station_features[0].station,
            name=f"Forecast for station '{station_features[0].station.name}'"
        )

    def predict_hour(self, hour_features: Features) -> Forecast:
        """
        Predict the irradiance for a specific hour using all the available
        algorithms
        """
        if len(self.models) == 0:
            raise AttributeError("Please set the models before forecast")

        algorithms_list = [
            model for model in self.models
            if (hour_features.station.name in model) and
               (hour_features.hour in model)
        ]

        results = [
            self.models[algorithm].predict(hour_features.data)
            for algorithm in algorithms_list
        ]

        return np.mean(results)

    def set_models(self, models: dict[str:Model]):
        self.models = models


@dataclass
class ForecastNewStation(ForecastMethod):
    """Type of forecast designated to NEW|UNKNOWN Stations"""

    def predict_station(self, station_features: list[Features]) -> Forecast:
        """Predict the irradiance for entire Station"""
        raise NotImplementedError()

    def predict_hour(self, hour_features: Features) -> Forecast:
        """Predict the irradiance for a specific hour and station"""

        if len(self.models) == 0:
            raise AttributeError("Please set the models before forecast")

        algorithms_list = [
            model for model in self.models
            if (hour_features.station.name in model) and
               (hour_features.hour in model)
        ]

        results = [
            self.models[algorithm].predict(hour_features.data)
            for algorithm in algorithms_list
        ]

        return np.mean(results)

    def set_models(self, models: dict[str:Model]):
        self.models = models


