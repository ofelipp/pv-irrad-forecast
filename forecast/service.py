# ! ./venv/bin/python3.10

from dataclasses import dataclass, field

from domain.data import Features, Forecast
from domain.model import Model
from domain.station import STATIONS_COORDINATES

from ports.inbound.forecast_use_case import ForecastUseCase
from forecast.loader import LoaderModelsInterface
from forecast.methods import ForecastMethod, ForecastMappedStation, ForecastNewStation

METHOD_FACTORY = {
    "mapped_station": ForecastMappedStation(),
    "new_station": ForecastNewStation(),
}


@dataclass
class ForecastService(ForecastUseCase):
    artifacts_path: str
    loader: LoaderModelsInterface
    forecaster: ForecastMethod = field(default=None)
    models: dict[str: Model] = field(default_factory=dict)

    def __post_init__(self):
        self.models = self.__get_models(path=self.artifacts_path)

    def predict(self, features: list[Features]) -> Forecast:
        """Predict solar irradiance based on a passed features"""

        self.__get_forecast_method(station=features[0].station.name)

        return self.forecaster.predict_station(features)

    def __get_models(self, path: str) -> dict:
        """Retrieve the models to predict solar irradiance"""
        return self.loader.load_models(path)

    def __get_forecast_method(self, station: str) -> None:
        """Retrieve the correct method to predict solar irradiance"""
        if station in STATIONS_COORDINATES:
            self.forecaster = METHOD_FACTORY["mapped_station"]
        else:
            self.forecaster = METHOD_FACTORY["new_station"]

        self.forecaster.set_models(models=self.models)
