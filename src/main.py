import json

from datatypes.passenger import Passenger

from car import Car
from city import City
from path_simple import PathSimple

from helpers import print_status


if __name__ == '__main__':
    city = City(10, 10)
    car = Car(PathSimple, city)

    # Get ride requests (array) json file. Each element represents 1 unit of time with an array of ride requests.
    with open('../requests.json', 'r') as f:
        time_units = json.load(f)

    for unit in time_units:

        # Load pickup requests into an array of the Passenger data type for better handling, comparisons, and validation
        pickup_requests = []
        for pickup_request in unit['requests']:
            try:
                passenger = Passenger(**pickup_request)
                pickup_requests.append(passenger)
            except TypeError as te:
                print("malformed passenger object")
            except ValueError as ve:
                print("passenger validation failed")

        city.add_pickup_requests(pickup_requests)
        print_status(city, car)  # this is a visualization tool to see the steps the car takes

        car.move()


