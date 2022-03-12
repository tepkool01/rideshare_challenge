from datatypes.passenger import Passenger
from datatypes.position import Position


class City:
    def __init__(self, columns=10, rows=10):
        # self.grid = [[None for _ in range(x)] for _ in range(y)]
        self.columns = columns
        self.rows = rows
        self.pickup_requests = []

    def get_pickup_positions(self) -> list[Position]:
        return [pickup_request.start_position for pickup_request in self.get_pickup_requests()]

    def get_pickup_requests(self) -> list[Passenger]:
        return self.pickup_requests

    def add_pickup_requests(self, pickup_requests: list[Passenger]) -> None:
        if len(pickup_requests) > 0:
            self.pickup_requests.extend(pickup_requests)
