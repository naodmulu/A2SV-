class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        if len(nums) < 3:
            return 0
        nums.sort()
        print(nums)
        for tar in range(len(nums)-1,-1,-1):
            l = 0
            r = tar-1
            while r>l:
                if nums[r] + nums[l] > nums[tar]:
                    ans += r-l
                    r -= 1
                elif nums[r] + nums[l] <= nums[tar]:
                    l += 1
        return ans
                