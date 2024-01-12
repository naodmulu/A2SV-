class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        new = cardPoints.copy()
        new.extend(cardPoints)
        ans = 0
        total_sum = 0
        l = len(cardPoints) - k
        for r in range(len(cardPoints)- k,len(cardPoints)+k):
        
            total_sum += new[r]
            if not(r-l < k):
                total_sum -= new[l]
                l += 1
            ans = max(ans,total_sum)
            
        return ans