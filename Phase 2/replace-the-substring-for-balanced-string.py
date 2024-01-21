class Solution:
    def balancedString(self, s: str) -> int:
        l = 0
        amount = len(s)//4
        s_count = Counter(s)
        checker = {}
        ans = float("inf")
        for key in s_count:
            if s_count[key] > amount:
                checker[key] = s_count[key] - amount
        r = 0
        # print(checker)
        while r < len(s):
            if s[r] in checker:
                checker[s[r]] -= 1
                
                # while checker[s[r]] < 0 :
                #     if s[l] in checker:
                #         checker[s[l]] += 1
                #     l += 1
            while all(value <= 0 for value in checker.values()) and l<len(s):
                if s[l] in checker:
                    checker[s[l]] += 1
                ans = min(ans,r-l+1)
                l += 1
            r += 1
        if ans == float("inf") or ans<0:
            return 0
        return ans
        
        