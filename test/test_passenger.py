import unittest
from datatypes.passenger import Passenger


class TestPassenger(unittest.TestCase):
    def test_passenger_valid(self):
        payload = {
            "name": "Elon",
            "start": [3, 5],
            "end": [8, 7]
        }
        passenger_type = Passenger(**payload)
        self.assertIs(type(passenger_type), Passenger)

    def test_passenger_invalid_start(self):
        payload = {
            "name": "Elon",
            "start": [3, 5, 9],
            "end": [8, 7]
        }
        with self.assertRaises(ValueError):
            Passenger(**payload)

    def test_passenger_invalid_end(self):
        payload = {
            "name": "Elon",
            "start": [3, 5],
            "end": [8, 7, 1]
        }
        with self.assertRaises(ValueError):
            Passenger(**payload)
