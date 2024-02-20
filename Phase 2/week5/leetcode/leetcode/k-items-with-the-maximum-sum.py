class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans=0
        for i in range(k):
            if numOnes:
                ans += 1
                numOnes -= 1
            elif numZeros:
                numZeros -= 1
            elif numNegOnes:
                ans -= 1
                numNegOnes -= 1
        return ans

        