from helpers import _find_closest_passenger
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
            # print("Has passengers!")
            destination = passengers[0].end_position  # Navigate to first passenger's spot / FIFO
        else:
            # print("Find nearest")
            destination = _find_closest_passenger(current_position, pickup_positions)  # Find closest pickup request

        # print(f"Navigating to: {destination}")

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

        # print(f"best path: {best_path}")
        if len(best_path) == 0:
            raise Exception("no path found")

        return best_path


