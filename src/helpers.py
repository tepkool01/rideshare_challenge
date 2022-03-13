from datatypes.position import Position
from city import City
from car import Car


def _find_closest_passenger(current_position: Position, pickup_positions: list[Position]) -> Position:
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
    return abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)


def print_status(city: City, car: Car):
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
