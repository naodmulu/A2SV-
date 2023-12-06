class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    
        total_time = 0

        for i in range(len(points) - 1):
            x = abs(points[i][0] - points[i + 1][0])
            y = abs(points[i][1] - points[i + 1][1])

            diagonal = min(x, y)

            x_remain = x - diagonal
            y_remain = y - diagonal
            
            remain = max(x_remain,y_remain)

            total_time += diagonal + remain

        return total_time