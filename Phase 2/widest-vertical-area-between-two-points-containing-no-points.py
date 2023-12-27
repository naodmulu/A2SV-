class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_di = []
        occur = set()
        for x,y in points:
            if x not in occur:
                x_di.append(x)
                occur.add(x)
        x_di.sort()
        ans = 0
        for i in range(len(x_di)-1):
            ans = max(ans,x_di[i+1] - x_di[i])
        
        return ans


        