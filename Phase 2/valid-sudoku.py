class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for li in board:
        #     print(li)
        
        aset = set()
        for i in range(9):
            aset.clear()
            for j in range(9):

                if board[i][j] != ".":
                    if board[i][j] in aset:
                        print(board[i][j])
                        print("bo")
                        return False
                    else:
                        aset.add(board[i][j])
        
        
        for i in range(9):
            aset.clear()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in aset:
                        print(board[j][i])
                        print("col")
                        return False
                    else:
                        aset.add(board[j][i])
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                aset.clear()
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if board[x][y] != ".":
                            if board[x][y] in aset:
                                return False
                            else:
                                aset.add(board[x][y])

        
        return True