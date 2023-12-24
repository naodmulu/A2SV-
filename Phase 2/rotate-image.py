class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = None
        jset = set()
        for i in range(len(matrix)):
            for j in range(len(matrix)):

                if j != i and (i,j) not in jset :
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
                    jset.add((j,i))
                    # print(i,j)
        
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

    # time = O(n**2)
    # space = O(n)
