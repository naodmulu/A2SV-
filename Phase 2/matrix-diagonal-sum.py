class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        val = 0
        
        for i in range(len(mat)):
            val += mat[i][i]
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i+j == len(mat)-1:
                    val += mat[i][j]
        
        if len(mat)%2:
            temp = len(mat)//2
            return val - mat[temp][temp]
        else:
            return val
        