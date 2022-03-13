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
        self.best_path = [Position(0, 1), Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)]  # todo dummy info

        self.city = city

    def move(self):
        print("car move")
        # Upon initialization, PathSimple will route to the nearest passenger
        # After picking up a passenger, it will then create a new path
        if len(self.best_path) == 0:
            print("Generating new path")
            self.best_path = self.path_finder.get_best_path(
                current_position=self.position,
                pickup_positions=self.city.get_pickup_positions()
            )

        # Moving to new location
        self.position = self.best_path.pop(0)

        # Are there any passengers at this location
        pickups = self.city.get_pickup_requests_by_location(location=self.position)
        if len(pickups) > 0:
            self.passengers.extend(pickups)  # Pick up the passengers
            self.city.remove_pickup_request(pickups)  # Remove from pickup queue in the city
            print(f"picked up passenger(s): {pickups}")

        # Is this a drop-off point?
        for passenger in self.passengers:
            if self.position == passenger.end_position:
                print(f"Dropping off {passenger}")
                self.passengers.remove(passenger)

    def pickup(self, passenger: Passenger) -> None: # todo USE ME (in move command)?!
        self.passengers.append(passenger)

    def dropoff(self, passenger: Passenger): # todo USE ME (in move command)!
        self.passengers.remove(passenger)

    def get_passengers(self) -> list[Passenger]:
        return self.passengers


