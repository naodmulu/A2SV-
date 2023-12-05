class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        sum_clock = 0
        sum_counter = 0
        length = len(distance)
        distance = distance *2
        x = min(start,destination)
        y = max(start,destination)
        
        for i in range(x,y):
            sum_clock += distance[i]
        for j in range(y,length + x):
            sum_counter += distance[j]

        return min(sum_counter,sum_clock)
            

        