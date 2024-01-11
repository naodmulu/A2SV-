class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        l = 0
        total = 0
        count = 0
        for r in range(len(nums)):
            total += nums[r]
            while (r-l+1)*nums[l] - total > k:
                total -= nums[l]
                l += 1
            count = max(count,r-l+1)
        
        return count
                

