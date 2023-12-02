class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        ans = 0
        temp = 0

        for roman in s:
            curr = values[roman]
            if curr > temp:
                ans += curr - (2*temp)
            else:
                ans += curr
            temp = curr
        return ans

        
        