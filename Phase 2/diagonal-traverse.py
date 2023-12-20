class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        index_sum = {}
        summ = None
        ans = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                summ = i + j
                if summ in index_sum:
                    index_sum[summ].append(mat[i][j])
                else:
                    index_sum[summ] = []
                    index_sum[summ].append(mat[i][j])
        for i in range(len(mat)+len(mat[0])-1):
            if i%2 == 0:
                ans.extend(index_sum[i][::-1])
            else:
                ans.extend(index_sum[i])

        return ans
                
        