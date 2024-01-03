class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        ans = 0
        # print(piles)
        for i in range(len(piles)//3):
            ans += piles[(i*2)+1]
        return ans

        # time complexity = O(nlogn)
        # space = O(1)
        
        