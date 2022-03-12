from dataclasses import dataclass, field
from .position import Position


@dataclass
class Passenger:
    name: str
    start: list[int]
    start_position: Position = field(init=False)
    end: list[int]
    # waiting_time: int = 0

    def __post_init__(self):
        if len(self.start) != 2:
            raise ValueError
        if len(self.end) != 2:
            raise ValueError
        # other validation here...
        self.start_position = Position(self.start[0], self.start[1])