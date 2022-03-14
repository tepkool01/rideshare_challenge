import unittest

from datatypes.position import Position
from src.car import Car
from src.city import City
from src.path_simple import PathSimple
from src.main import run_rideshare


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        self.city = City(10, 10)
        self.car = Car(PathSimple, self.city)

    def test_happy_run_rideshare(self):
        run_rideshare(
            [{
                "requests": [
                    {
                        "name": "Elon",
                        "start": [3, 5],
                        "end": [8, 7]
                    },
                    {
                        "name": "George",
                        "start": [1, 2],
                        "end": [4, 3]
                    }
                ]
            }]
            , self.car, self.city)
        self.assertEqual(self.car.position, Position(x=8, y=7))

    def test_move_without_requests(self):
        run_rideshare([{"requests": []}], self.car, self.city)
        self.assertEqual(self.car.position, Position(x=0, y=0))

    def test_en_route_pickup(self):
        run_rideshare([
            {
                "requests": [
                    {
                        "name": "Elon",
                        "start": [3, 5],
                        "end": [8, 7]
                    },
                    {
                        "name": "George",
                        "start": [1, 2],
                        "end": [4, 3]
                    }
                ]
            },
            {
                "requests": [
                    {
                        "name": "Michael",
                        "start": [2, 2],
                        "end": [9, 9]
                    }
                ]
            }
        ], self.car, self.city)
        print(self.car.position)
        self.assertEqual(self.car.position, Position(x=8, y=7))
