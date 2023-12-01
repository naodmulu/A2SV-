class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)-1
        n = len(matrix[0])-1

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True