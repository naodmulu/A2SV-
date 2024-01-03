class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = []
        for word in s:
            if 97 <= ord(word.lower()) <= 122 or '0' <= word <= '9' :
                check.append(word.lower())  
        for i in range(len(check)//2):
            if check[i] != check[len(check)-1-i]:
                return False
        return True