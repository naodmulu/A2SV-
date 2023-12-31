class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums = nums[::-1]

        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return sum(nums[i:i+3])
        
        return 0