class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = 0
        for i in range(len(nums)):
            step = max(step,nums[i]+i)
            if step == i and i != len(nums)-1:
                return False
        return True
            