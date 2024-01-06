class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        val = sum(nums[0:k])/k
        temp = sum(nums[0:k])
        for i in range(k,len(nums)):
            print(temp)
            temp += nums[i] - nums[i-k]
            val = max(val,temp/k)

            
        return val
        