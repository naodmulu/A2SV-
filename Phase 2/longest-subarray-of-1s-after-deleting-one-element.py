class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        ans = 0
        zero = False
        while i < len(nums) and j <len(nums):
            if nums[i] == 0:
                if i == j:
                    i += 1
                    j += 1
                    zero = False
                else:
                    i += 1
                    zero = False
            else:
                if nums[j] == 1 and not zero :
                    ans = max(ans,j-i+1)
                    j += 1
                elif nums[j] == 0 and not zero:
                    zero = True
                    j += 1
                elif nums[j] == 1 and zero:
                    ans = max(ans,j-i)
                    j += 1
                elif nums[j] == 0 and zero:
                    i += 1
        if ans == len(nums):
            return ans -1
        return ans