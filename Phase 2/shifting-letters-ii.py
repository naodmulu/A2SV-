class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0 for _ in range(len(s)+1) ]
        for l,r,d in shifts:
            if d:
                c = 1
            else:
                c = -1
            prefix[l] += c
            prefix[r+1] -= c

        total = 0
        for i in range(len(prefix)):
            total += prefix[i]
            prefix[i] = total 
        
        # a = 97
        # print(prefix)
        ans = []
        for i in range(len(s)):
            temp =ord(s[i])%97
            val = abs(prefix[i])%26
            # print(temp)
            if prefix[i] >= 0:
                char=chr(97+(val+temp)%26)
                
            else:
                if temp - val < 0:
                    # print("x")
                    # print(26-(temp-val),temp-val)
                    char = chr(97+26-abs(temp-val))
                else:
                    char = chr(97+(temp-val))
            # print(temp,char)
            ans.append(char)
            
        return "".join(ans)
        