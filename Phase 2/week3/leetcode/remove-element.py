class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        place = 0
        seek = 0
        count = len(nums)
        # print(count)
        while seek < len(nums):
            if nums[seek] == val:
                seek += 1
                count -= 1
            elif nums[seek] != val:
                nums[seek],nums[place] = nums[place],nums[seek]
                place += 1
                seek += 1
        # print(nums,count)
        return count
            