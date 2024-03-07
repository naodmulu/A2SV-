class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations == [0]:
            return 0
        ans = 0
        l = 0
        r = len(citations)-1
        size = len(citations)
        while l <= r:
            mid = (l+r)//2
            if citations[mid] >= size - mid:
                ans = size - mid
                r = mid -1
            else:
                l = mid +1
        return ans
        