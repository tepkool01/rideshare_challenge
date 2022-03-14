from datatypes.passenger import Passenger
from datatypes.position import Position
from city import City
from car import Car


def parse_pickup_requests(pickup_requests: []) -> list[Passenger]:
    """
    Load pickup requests into an array of the Passenger data type for better handling, comparisons, and validation
    :param pickup_requests: array of json objects that will be destructured into a passenger data type
    :return: a list of passenger data types
    """
    parsed_requests = []
    for pickup_request in pickup_requests:
        try:
            passenger = Passenger(**pickup_request)
            parsed_requests.append(passenger)
        except TypeError as te:
            print("malformed passenger object: ", str(te))
        except ValueError as ve:
            print("passenger validation failed: ", str(ve))
    return parsed_requests


def _find_closest_passenger(current_position: Position, pickup_positions: list[Position]) -> Position:
    """
    locates the closest point from an array of Positions, from a current Position.
    """
    if len(pickup_positions) == 0:
        return current_position

    closest_request = pickup_positions[0]
    shortest_distance = get_path_distance(current_position, closest_request)
    for pickup_request in pickup_positions[1:]:
        if get_path_distance(current_position, pickup_request) < shortest_distance:
            closest_request = pickup_request
            shortest_distance = get_path_distance(current_position, pickup_request)

    return closest_request


def get_path_distance(pos1: Position, pos2: Position):
    """
    returns the distance between 2 points given orthogonal moves. used in finding the closest passenger. could be useful
    in other algorithms
    """
    return abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)


def print_status(city: City, car: Car):
    """
    This prints to the screen the entire grid and the status of all outstanding passengers and car location
    """
    pickup_requests = city.get_pickup_requests()
    print(f"{len(pickup_requests)} outstanding requests.")

    # Grab all pickup positions
    customer_positions = []
    for req in pickup_requests:
        customer_positions.append(req.start_position)

    # Create grid, detect Car location and Pickup request locations
    for y in range(city.rows):
        for x in range(city.columns):
            current_position = Position(x, y)
            if current_position == car.position:
                print(" C ", end='')
            elif current_position in customer_positions:
                print(" P ", end='')
            else:
                print(" _ ", end='')

        print("")
