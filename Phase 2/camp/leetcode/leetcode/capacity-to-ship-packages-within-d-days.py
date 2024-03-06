class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checker(mid):
            r = 0
            for i in range(days):
                total = 0
                while r < len(weights) and total + weights[r] <= mid:
                    total += weights[r]
                    r += 1
                if r >= len(weights):
                    return True
            return False
        
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high)//2
            if checker(mid):
                high = mid -1
            else:
                low = mid +1
        return low
