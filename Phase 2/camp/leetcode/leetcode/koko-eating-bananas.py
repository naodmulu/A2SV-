class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort(reverse = True)
        def checker(mid,piles):
            hour = 0
            i = 0
            while i < len(piles):
                hour += ceil(piles[i]/mid)
                i += 1

            return True if hour <= h else False
        
        
        low,high = 1, max(piles)
        
        ans = high
        while low <= high:
            mid = (low+high)//2
            if checker(mid,piles[:]):
                ans = mid
                high = mid -1
            else:
                low = mid +1

        return ans
