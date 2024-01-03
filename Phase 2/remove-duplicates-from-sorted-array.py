class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seek = 0
        placeholder = 1

        while placeholder < len(nums):
            while placeholder < len(nums) and nums[seek] == nums[placeholder]:
                placeholder += 1
            if placeholder < len(nums):
                nums[seek+1],nums[placeholder] = nums[placeholder],nums[seek+1]
                # print(nums,placeholder,seek)
                seek += 1
                placeholder +=1
        return seek +1     

            
        