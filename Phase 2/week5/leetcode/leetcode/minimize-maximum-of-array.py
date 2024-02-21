class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            nums[i] = ceil(total/(i+1))
            
        return max(nums)
        