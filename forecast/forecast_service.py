# ! ./venv/bin/python3.10

from dataclasses import dataclass, field

from domain.data import Data
from domain.model import Model

from ports.inbound.forecast_use_case import ForecastUseCase
from forecast.loader import LoaderModelsInterface

MODELS_PATH = "artifacts/"


@dataclass
class ForecastService(ForecastUseCase):
    loader: LoaderModelsInterface
    models: dict[str: Model] = field(default_factory=dict)

    def __post_init__(self):
        self.models = self.get_models(path=MODELS_PATH)

    def get_models(self, path: str) -> dict:
        return self.loader.load_models(path)

    def predict(self, features: Data) -> Data:
        return Data(data=[0, 0, 0])
