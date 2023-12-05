class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            max_one = max(count,max_one)        

        return max_one
        