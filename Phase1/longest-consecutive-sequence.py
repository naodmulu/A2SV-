class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        start = 0
        seq = 0
        for i in set_nums:
            if i-1 not in set_nums:
                start = i
                seq = 1
            
            while start + 1 in set_nums:
                start += 1
                seq += 1
            
            longest = max(longest,seq)
        return longest
