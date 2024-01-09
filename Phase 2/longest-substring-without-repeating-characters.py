class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        l = 0
        ans = 0
        for r in range(len(s)):
            # print(dic)
            temp = s[r]

            if temp in dic:
                l = max(l,dic[temp] + 1)

            dic[temp] = r
            # print(l,r)
            ans = max(ans, r - l + 1)

        return ans

        # time complexity = O(n)
        # space = O(1)
        