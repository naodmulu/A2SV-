class Solution:
    def minWindow(self, s: str, t: str) -> str:
        check = Counter(t)
        r = 0
        l = 0 
        ans  = [len(s),len(s)]
        temp = len(s) +1 
        while r < len(s) and l < len(s):
            if s[r] in check:
                check[s[r]] -= 1
            
            while all(value <= 0 for value in check.values()) and l<len(s):
                if s[l] in check:
                    check[s[l]] += 1
                if r-l+1 < temp:
                    ans = [l,r]
                    temp = r-l+1
                l += 1
            r += 1
        print(ans)   
        return s[ans[0]:ans[1]+1]
