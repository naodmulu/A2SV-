class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        prefix = 0
        total= sum(nums)
        ans = []
        for i in range(len(nums)):
            total -= nums[i]
            
            temp = (nums[i] * i) - prefix
            temp += total - nums[i]*(len(nums)-i-1)
            
            ans.append(temp)
            prefix += nums[i]
        return ans