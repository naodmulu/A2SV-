class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        count = 0
        arr = [[0 for _ in range(n)] for _ in range(m)]
        for x,y in walls:
            arr[x][y] = "W"
        for x,y in guards:
            arr[x][y] = "G"

        for i in range(m):
            seen_guard = False
            for j in range(n):
                if seen_guard and arr[i][j] == 0:
                    arr[i][j] = 1
                elif arr[i][j] == "G":
                    seen_guard = True
                elif arr[i][j] == "W":
                    seen_guard = False
            seen_guard = False
            for j in range(n-1,-1,-1):
                if seen_guard and arr[i][j] == 0:
                    arr[i][j] = 1
                elif arr[i][j] == "G":
                    seen_guard = True
                elif arr[i][j] == "W":
                    seen_guard = False

        for j in range(n):
            seen_guard = False
            for i in range(m):
                if seen_guard and arr[i][j] == 0:
                    arr[i][j] = 1
                elif arr[i][j] == "G":
                    seen_guard = True
                elif arr[i][j] == "W":
                    seen_guard = False
            seen_guard = False
            for i in range(m-1,-1,-1):
                if seen_guard and arr[i][j] == 0:
                    arr[i][j] = 1
                elif arr[i][j] == "G":
                    seen_guard = True
                elif arr[i][j] == "W":
                    seen_guard = False
        for i in range(m):
            for j in range(n):
                if arr[i][j] == 0:
                    count += 1

        return count