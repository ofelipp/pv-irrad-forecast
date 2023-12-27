from dataclasses import dataclass
from geopy import distance


@dataclass
class Coordinates:
    latitude: float | None
    longitude: float | None

    def __post_init__(self):
        self.validate()

    def as_tuple(self) -> tuple:
        return tuple([self.latitude, self.longitude])

    def as_dict(self) -> dict[str:float]:
        return {"latitude": self.latitude, "longitude": self.longitude}

    def validate(self):
        if (self.latitude is None) or (self.longitude is None):
            self.latitude = None
            self.longitude = None
            return

        if (self.latitude > abs(90)) or (self.longitude > abs(90)):
            self.latitude = None
            self.longitude = None


def calculate_distance_between_coordinates(
    coordinates_1: Coordinates,
    coordinates_2: Coordinates,
) -> float:
    """Calculate the distance in km between two coordinates"""
    return distance.distance(
        coordinates_1.as_tuple(), coordinates_2.as_tuple()
    ).km
