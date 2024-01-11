class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 
        if len(nums) == 0:
            return 0

        l = 0
        r = 0
        ans = float('inf')
        summ = 0
        while r < len(nums):
            
            summ += nums[r]
            r += 1
            while summ >= target:
                summ -= nums[l]
                ans = min(ans,r-l)
                l +=1
        if ans != float("inf"):
            return ans
        else:
            return 0
    
    # time complexity = O(n)
    # space = O(1)

        