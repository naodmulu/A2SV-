class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        temp = 0
        ans = 0
        i = 0
        while i < len(nums):
            if temp+1 < nums[i]:
                ans += 1
                temp += temp + 1
            else:
                temp += nums[i]
                i += 1
            if temp >= n:
                return ans
                
        while temp < n:
            ans+= 1
            temp += temp +1
        return ans
        