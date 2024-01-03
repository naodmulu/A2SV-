class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        ans = 0
        while l != r:
            if nums[r] + nums[l] >= target:
                r -= 1
            else:
                # print(ans)
                ans += r - l
                l += 1
        return ans
        