class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        in_sum = [0 for i in range(len(nums)+1)]
        in_sum[0] = right
        val = right
        for i in range(len(nums)):
            if nums[i] == 0:
                left += 1
                in_sum[i+1] = left + right
                val = max(val,in_sum[i+1])
            elif nums[i] == 1:
                right -= 1
                in_sum[i+1] = left + right
                val = max(val,in_sum[i+1])
        print(in_sum,max)
        return [i for i in range(len(in_sum)) if in_sum[i] == val]


        