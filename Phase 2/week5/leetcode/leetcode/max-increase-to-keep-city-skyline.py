class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax = [max(r) for r in grid]
        colMax = [max(c) for c in zip(*grid)]
        # print(rowMax,colMax)
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                temp = min(rowMax[r],colMax[c])
                if temp - grid[r][c]> 0:
                    ans+= temp - grid[r][c]
        return ans