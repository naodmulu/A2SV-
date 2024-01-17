class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefix = [[0]]
        else:
            self.prefix = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                i = row + 1
                j = col + 1
                self.prefix[i][j] = self.prefix[i-1][j] + self.prefix[i][j-1] - self.prefix[i-1][j-1] + matrix[row][col]

        #     print(self.prefix[row+1])
        # print(len(self.prefix),len(self.prefix[0]))
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1 = row1 +1
        c1 = col1 +1
        r2 = row2 + 1
        c2 = col2 +1
        # print(r1,r2,c1,c2)
        submatrix_sum = self.prefix[r2][c2] - self.prefix[r2][c1 - 1] - self.prefix[r1 - 1][c2] + self.prefix[r1 - 1][c1 - 1]
        return submatrix_sum


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)