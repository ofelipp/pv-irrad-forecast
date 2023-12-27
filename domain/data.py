from dataclasses import dataclass, field
import numpy as np

from domain.station import Station

ORDER_FEATURES = [
    "temperature_C", "cloud_cover_percentual", "altitude_m"
]


@dataclass
class Data:
    data: np.array
    name: str = field(default=None)


@dataclass
class Features(Data):
    hour: str = field(default=None)
    station: Station = field(default=None)
    features_names: list = field(default_factory=ORDER_FEATURES)


@dataclass
class Forecast(Data):
    data: dict
    station: Station = field(default=None)

    def as_dict(self):
        return {
            "station": self.station.name,
            "coordinates": self.station.coordinates.as_dict(),
            "forecast": {
                f"hour_{hour}": forecast
                for hour, forecast in self.data.items()
            }
        }













