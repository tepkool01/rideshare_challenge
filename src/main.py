import json

from car import Car
from city import City
from path_simple import PathSimple

from helpers import print_status, parse_pickup_requests


def run_rideshare(ride_requests: [], car: Car, city: City) -> None:
    """
    runs the program by loading in the ride requests into the grid/city and looping the car until it completes
    """
    for unit in ride_requests:
        pickup_requests = parse_pickup_requests(unit['requests'])  # load requests into Passenger data type
        city.add_pickup_requests(pickup_requests)
        # print_status(city, car)  # this is a visualization tool to see the steps the car takes
        car.move()

    # In case the JSON array/payload terminated without finishing all the requests, this will complete them
    while len(city.get_pickup_requests()) > 0 or len(car.passengers) > 0:
        # print_status(city, car)
        car.move()


if __name__ == '__main__':
    city = City(10, 10)  # Create a 10x10 (x,y) grid of the city, per the requirements
    car = Car(PathSimple, city)  # Load in an algorithm for the car to determine its optimal path

    # Get ride requests (array) json file. Each element represents 1 unit of time with an array of ride requests.
    with open('requests.json', 'r') as f:
        ride_requests = json.load(f)

    run_rideshare(ride_requests, car, city)
