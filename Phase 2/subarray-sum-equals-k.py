class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        dic = {0:1}

        for num in nums:
            prefix += num
            temp = prefix - k
            if temp in dic:
                count += dic[temp]
            if prefix in dic:
                dic[prefix] += 1
            else:
                dic[prefix] = 1
        
        return count

        