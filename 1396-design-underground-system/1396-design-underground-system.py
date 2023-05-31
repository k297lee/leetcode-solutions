class UndergroundSystem:

    def __init__(self):
        self.times = {}
        self.curr = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.curr[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startTime, start = self.curr[id]
        delta = t - startTime
        totalTime = 0
        times = 0
        if (start, stationName) in self.times.keys():
            totalTime = self.times[(start, stationName)][0]
            times = self.times[(start, stationName)][1]
        self.times[(start, stationName)] = (totalTime + delta, times + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, times = self.times[(startStation, endStation)]
        return totalTime / times


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)