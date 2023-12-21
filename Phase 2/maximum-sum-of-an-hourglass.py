class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        val = 0
        row = len(grid)
        col = len(grid[0])
        tval = 0
        
        for i in range(row-2):
            for j in range(col-2):
                tval = 0
                for pos in range(3):
                    tval += grid[i][j+pos]
                tval += grid[i+1][j+1]
                for pos in range(3):
                    tval += grid[i+2][j+pos] 
                
                val = max(tval,val)
        
        return val
        
                    
