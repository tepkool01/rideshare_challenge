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
        # No path established, find new path
        if len(self.best_path) == 0:
            self.best_path = self.path_finder.get_best_path(
                current_position=self.position,
                pickup_positions=self.city.get_pickup_positions()
            )

        self.position = self.best_path.pop(0)
        #todo pickup passenger, and get new path?
        print("car move")

    def pickup(self, passenger: Passenger) -> None:
        self.passengers.append(passenger)

    def dropoff(self, passenger: Passenger):
        self.passengers.remove(passenger)

    def get_passengers(self) -> list[Passenger]:
        return self.passengers


