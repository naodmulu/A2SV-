class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        if len(palindrome)< 2:
            return ""
        length = len(palindrome)//2
        flag = False
        ans = [char for char in palindrome]
        for i in range(length):
            if ans[i] != "a":
                temp = ans[i]
                ans[i] = "a"
                flag = True
                break
        if not flag:
            ans[-1] = "b"
        
        return "".join(ans)

        