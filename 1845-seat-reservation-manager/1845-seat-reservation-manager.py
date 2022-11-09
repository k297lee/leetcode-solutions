class SeatManager:

    def __init__(self, n: int):
        self.available = list(range(1, n + 1))
        heapq.heapify(self.available)
        self.reserved = set()

    def reserve(self) -> int:
        seat = heapq.heappop(self.available)
        self.reserved.add(seat)
        return seat

    def unreserve(self, seatNumber: int) -> None:
        self.reserved.remove(seatNumber)
        heapq.heappush(self.available, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)