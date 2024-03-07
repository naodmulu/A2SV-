class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        checker = [matrix[i][0] for i in range(len(matrix))]
        print(checker)
        l = 0
        r = len(checker)-1
        temp = 0
        while l <= r:
            mid = (l+r)//2
            if checker[mid] > target:
                r = mid -1
            else:
                l = mid + 1
                 
        find = r
        l = 0
        r = len(matrix[r])-1
        while l <= r:
            mid = (l + r)//2
            if matrix[find][mid] > target:
                r = mid -1
            elif matrix[find][mid] < target:
                l = mid +1
            else:
                return True
        return False