class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start = [(intervals[i][0],i) for i in range(len(intervals))]
        start.sort()
        ans = []

        def binary(x):
            l = 0
            r = len(start)-1
            while l <= r:
                mid = (l+r)//2
                if start[mid][0] >= x:
                    r = mid-1
                else:
                    l = mid +1
            return l

        for s,e in intervals:
            temp = binary(e)
            if temp >= len(intervals):
                ans.append(-1)
            else:
                ans.append(start[temp][1])

        return ans