class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp = nums.copy()
        nums.extend(temp)
        return nums