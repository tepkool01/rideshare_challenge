from interfaces.path_algorithm_interface import PathAlgorithmInterface
from datatypes.position import Position


class PathSimple(PathAlgorithmInterface):
    @staticmethod
    def get_best_path(current_position: Position, pickup_positions: list[Position]) -> list[Position]:
        closest_passenger = _find_closest_passenger(current_position, pickup_positions)

        # If has passengers, then navigate to 1st passenger's spot

        # else, find closest pickup request, and navigate there


        # Alternate between x and y to stay in 'middle' most times

        print(current_position)
        print(closest_passenger)
        return [Position(0, 0)]


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