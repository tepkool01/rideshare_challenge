from interfaces.path_algorithm_interface import PathAlgorithmInterface
from datatypes.position import Position
from datatypes.passenger import Passenger


class PathSimple(PathAlgorithmInterface):
    @staticmethod
    def get_best_path(current_position: Position, passengers: list[Passenger], pickup_positions: list[Position]) -> list[Position]:
        """
        Gets the best path based on current position, passengers, and potential pickup locations in the city
        :param current_position: Car's current position
        :param passengers: Car's passengers, which holds destination information
        :param pickup_positions: Availabile pickup points for the car; used when the car has no passengers
        :return: A list of positions the car should navigate towards
        """
        if len(passengers) > 0:
            print("Has passengers!")
            destination = passengers[0].end_position  # Navigate to first passenger's spot / FIFO
        else:
            print("Find nearest")
            destination = _find_closest_passenger(current_position, pickup_positions)  # Find closest pickup request

        print(f"Navigating to: {destination}")

        # Todo: do 2 while loops, if one picks up more passengers along the way, that's the better path
        best_path = []
        x = current_position.x
        y = current_position.y
        while x != destination.x or y != destination.y:
            if x < destination.x:
                x += 1
            elif x > destination.x:
                x -= 1
            elif y < destination.y:
                y += 1
            elif y > destination.y:
                y -= 1

            best_path.append(Position(x, y))

        # best_path_y = []
        # x = current_position.x
        # y = current_position.y
        # while x != destination.x or y != destination.y:
        #     if x < destination.x:
        #         x += 1
        #     elif x > destination.x:
        #         x -= 1
        #     elif y < destination.y:
        #         y += 1
        #     elif y > destination.y:
        #         y -= 1
        #
        #     best_path.append(Position(x, y))

        print(f"best path: {best_path}")

        return best_path


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