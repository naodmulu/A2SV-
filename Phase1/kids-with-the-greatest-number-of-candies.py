class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most = max(candies)
        answer = []
        for i in candies:
            if i + extraCandies >= most:
                answer.append(True)
            else:
                answer.append(False)
        
        return answer
        