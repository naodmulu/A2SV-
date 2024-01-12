class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0
        h = set()
        l = 0
        temp = 0
        for r in range(len(nums)):
            while nums[r] in h:
                h.remove(nums[l])
                ans -= nums[l]
                l += 1
            h.add(nums[r])
            ans += nums[r]
            temp = max(ans,temp)
        
        return temp
        