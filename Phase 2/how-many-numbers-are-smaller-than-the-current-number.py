class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        sorted_index = {}
        for i,num in enumerate(nums_sorted) :
            if num not in sorted_index:
                sorted_index[num] = i

        for i in range(len(nums)):
            nums[i] = sorted_index[nums[i]]

        return nums