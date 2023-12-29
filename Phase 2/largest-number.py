class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j][0] < nums[j+1][0]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                elif nums[j][0] == nums[j+1][0]:
                    if nums[j]+nums[j+1] < nums[j+1]+nums[j]:
                        nums[j],nums[j+1] = nums[j+1],nums[j]



        return str(int("".join(nums)))
        
        