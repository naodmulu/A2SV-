class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def checker(val):
            total = 0
            for i in range(len(nums)):
                total += ceil(nums[i]/val)
            return total <= threshold
        l = 1
        r = max(nums)
        while l <= r:
            mid = (l+r)//2
            if checker(mid):
                r = mid -1
            else:
                l = mid +1
        
        return l

        