# ! ./venv/bin/python3.10

from dataclasses import dataclass, field
import dotenv
import os

from ports.inbound.poller import Poller
from ports.inbound.forecast_use_case import ForecastUseCase

from adapters.inbound.sqs_poller import SQSPoller
from forecast.forecast_service import ForecastService
from forecast.loader import S3LoaderModels


@dataclass
class DependencyInjection:
    poller: Poller = field(default=None)
    forecaster: ForecastUseCase = field(default=None)

    def __post_init__(self):
        dotenv.load_dotenv()
        self.poller = self.get_poller()
        self.forecaster = self.get_forecaster()

    @staticmethod
    def get_poller():
        return SQSPoller()

    @staticmethod
    def get_forecaster():
        return ForecastService(
            loader=S3LoaderModels(bucket=os.environ["PROJECT_BUCKET"]),
            artifacts_path=os.environ["ARTIFACTS_PATH"]
        )
