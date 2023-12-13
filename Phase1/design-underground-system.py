class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.time_taken = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = [stationName,t]
        # print("check in",self.check_in)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        location = tuple([self.check_in[id][0],stationName])
        if location not in self.time_taken:
            self.time_taken[location] = []
        self.time_taken[location].append(abs(self.check_in[id][1]-t))
        # print("check out",self.time_taken,self.check_in[id][1],t)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        location = tuple([startStation,endStation])
        length = len(self.time_taken[location])
       
        return sum(self.time_taken[location]) / length


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)