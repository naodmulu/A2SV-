class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        occur = defaultdict(int)
        ans = 0

        for r in range(len(s)):
            occur[s[r]]+=1

            while (r-l+1) - max(occur.values()) > k:
                occur[s[l]]-=1
                
                if occur[s[l]] == 0:
                    del occur[s[l]]
                l += 1
            ans = max(ans,r-l+1)
        return ans
        