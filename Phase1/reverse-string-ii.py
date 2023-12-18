class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k == 1:
            return s
        flag = 1
        ans = ''
        count = 0
        temp = ''
        for char in s:
            temp += char
            count += 1
            if count == k and flag == 1:
                count = 0
                ans += temp[::-1]
                temp = ''
                flag = 0
            elif count == k and flag == 0:
                count = 0
                ans += temp
                temp = ''
                flag = 1

        if flag == 1:
            return ans + temp[::-1]
        else:
            return ans + temp    
        

        
        