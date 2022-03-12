from datatypes.position import Position
from city import City
from car import Car


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