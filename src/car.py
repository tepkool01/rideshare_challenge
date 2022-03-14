from typing import Type

from city import City
from datatypes.passenger import Passenger
from datatypes.position import Position
from interfaces.path_algorithm_interface import PathAlgorithmInterface


class Car(object):
    def __init__(self, path_finder: Type[PathAlgorithmInterface], city: City):
        self.path_finder = path_finder
        self.passengers = []
        self.position = Position(0, 0)
        self.best_path = []
        self.city = city

    def move(self):
        print(f"car position: x={self.position.x},y={self.position.y}; passengers: {self._join_passenger_names(self.passengers)}")

        # Upon initialization, PathSimple will route to the nearest passenger
        # After picking up a passenger, it will then create a new path
        if len(self.best_path) == 0:
            try:
                self.best_path = self.path_finder.get_best_path(
                    current_position=self.position,
                    passengers=self.passengers,
                    pickup_positions=self.city.get_pickup_positions()
                )
            except Exception as e:
                print(str(e))
                return

        # Moving to new location
        self.position = self.best_path.pop(0)

        # Evaluate this location en route for any people to pick up, drop off, etc
        self.perform_passenger_exchanges()

    def perform_passenger_exchanges(self):
        # Are there any passengers at this location
        pickups = self.city.get_pickup_requests_by_location(location=self.position)
        if len(pickups) > 0:
            self.pickup(pickups)

        # Is this a drop-off point?
        for passenger in self.passengers:
            if self.position == passenger.end_position:
                self.dropoff(passenger)

    def pickup(self, passengers: list[Passenger]) -> None:
        print(f"picking up passenger(s): {self._join_passenger_names(passengers)}")
        self.passengers.extend(passengers)  # Pick up the passengers
        self.city.remove_pickup_request(passengers)  # Remove from pickup queue in the city

    def dropoff(self, passenger: Passenger):
        print(f"dropping off {passenger.name}")
        self.passengers.remove(passenger)

    @staticmethod
    def _join_passenger_names(passengers) -> str:
        return ', '.join([p.name for p in passengers])
