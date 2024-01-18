class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = []
        prefix = [1]

        # prefix
        total = 1
        for i in range(len(nums)):
            total *= nums[i]
            prefix.append(total)
        # print(prefix)
        # suffix
        total = 1
        for i in range(len(nums)-1,-1,-1):
            total *= nums[i]
            suffix.append(total)
        suffix = suffix[::-1]
        suffix.append(1)
        # print(suffix)
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[i+1])

        return ans 

        
        