from dataclasses import dataclass, field
import json

from domain.coordinates import Coordinates, calculate_distance_between_coordinates


with open("artifacts/stations/stations_coordinates.json", "rb") as filename:
    STATIONS_COORDINATES = json.load(filename)

with open("artifacts/stations/stations_neighbors.json", "rb") as filename:
    STATIONS_NEIGHBORS = json.load(filename)


@dataclass
class Station:
    name: str = field(default=None)
    coordinates: Coordinates = field(default=None)
    nearest_stations: list = field(default=None)

    def __post_init__(self):
        """
        Get Coordinates if station name is mapped or get the nearest stations
        based on Coordinates passed
        """
        if self.name in STATIONS_COORDINATES:
            self.coordinates = self.get_coordinates_from_station()

        self.nearest_stations = self.get_nearest_stations(number=3)

    def get_nearest_stations(self, number: int):
        """Retrieves the nearest stations from the Coordinates."""
        if self.name in STATIONS_NEIGHBORS:
            return STATIONS_NEIGHBORS[self.name][:number]
        else:
            station_distance = self.__calculate_distance_from_stations()
            return [station for station, distance in station_distance][:number]

    def get_coordinates_from_station(self) -> Coordinates:
        """From a know station return the Coordinates information"""
        return Coordinates(
            latitude=STATIONS_COORDINATES[self.name]["latitude"],
            longitude=STATIONS_COORDINATES[self.name]["longitude"]
        )

    def __calculate_distance_from_stations(self) -> list[tuple[str, float]]:
        """Calculate the distance between this station to the others"""

        if self.coordinates is None:
            raise ValueError("Coordinates are empty")

        distances = {}
        for station in STATIONS_COORDINATES:
            distances[station] = calculate_distance_between_coordinates(
                self.coordinates, STATIONS_COORDINATES[station]
            )

        return sorted(distances.items(), key=lambda pair: pair[1])
