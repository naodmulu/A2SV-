class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        ans = 0
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for key in count:
            freq = count[key]

            if freq > 1:
                ans += (freq*(freq-1))/2
        return int(ans) 
        