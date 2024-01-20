class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = [0]
        total = 0
        for num in nums:
            total += num
            prefix.append(total)
        print(prefix,total)
        for i in range(1,len(prefix)):
            if prefix[i-1] == total - prefix[i]:
                return i - 1
        return -1
        