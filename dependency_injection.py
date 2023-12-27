# ! ./venv/bin/python3.10

from dataclasses import dataclass, field
import os

from ports.inbound.poller_use_case import PollerUseCase
from ports.inbound.forecast_use_case import ForecastUseCase

from adapters.inbound.sqs_poller import SQSPoller
from forecast.service import ForecastService
from forecast.loader import S3LoaderModels


@dataclass
class DependencyInjection:
    poller: PollerUseCase = field(default=None)
    service: ForecastUseCase = field(default=None)

    def __post_init__(self):
        self.poller = self.get_poller()
        self.service = self.get_forecast_service()

    @staticmethod
    def get_poller():
        return SQSPoller()

    @staticmethod
    def get_forecast_service():
        return ForecastService(
            loader=S3LoaderModels(bucket=os.environ["PROJECT_BUCKET"]),
            artifacts_path=os.environ["ARTIFACTS_PATH"]
        )
