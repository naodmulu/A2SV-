class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        print(points)
        l = 0
        count = 0
        while l < len(points):
            r = l+1
            high = points[l][1]
            low = points[l][0]
            while r < len(points):
                if points[l][1] < points[r][0]:
                    break
                r += 1
            count += 1
            l = r


        return count
        