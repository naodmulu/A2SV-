class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0 for _ in range(n+1) ]
        for first,last,seats in bookings:
            prefix[first-1] += seats
            prefix[last] -= seats
            # print(prefix)
        total = 0
        for i in range(len(prefix)):
            total += prefix[i]
            prefix[i] = total
        
        prefix.pop()
        return prefix