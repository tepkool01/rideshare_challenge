from abc import ABC, abstractmethod

from datatypes.position import Position


class PathAlgorithmInterface(ABC):
    @staticmethod
    @abstractmethod
    def get_best_path(current_position: Position, pickup_positions: list[Position]) -> list[Position]:
        pass
