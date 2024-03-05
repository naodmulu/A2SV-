class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_max = len(board)
        col_max = len(board[0]) 
        seen = set()
        
        def helper(i,j,idx):
            if idx == len(word):
                return True
            if i < 0 or i >= row_max or j < 0 or j >= col_max:
                return
            if board[i][j] != word[idx]:
                return
            if (i,j) in seen:
                return

            seen.add((i,j))
            if helper(i+1, j,idx+1):
                return True
            if helper(i-1, j,idx+1):
                return True
            if helper(i, j+1,idx+1):
                return True
            if helper(i, j-1,idx+1):
                return True
            seen.remove((i,j))

            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    val = helper(i,j,0)
                    if val:
                        return True
        
        return False
        