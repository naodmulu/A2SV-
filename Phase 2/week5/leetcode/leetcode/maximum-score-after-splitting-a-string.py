class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        total = 0
        for i in range(len(s)):
            if s[i] == "1":
                total += 1
        zeros = 0
        for i in range(len(s)-1):
            if s[i] == "0":
                zeros += 1
            if s[i] == "1":
                total -= 1
            print(total + zeros)
            ans = max(ans,total + zeros)
        return ans