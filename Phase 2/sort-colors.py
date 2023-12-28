class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums)):
            change = i
            for j in range(i,len(nums)):
                
                if nums[change] > nums[j]:
                    change = j

            nums[i],nums[change] = nums[change],nums[i]