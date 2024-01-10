class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {"u","o","i","e","a"}
        r = k-1
        l = 0
        count = 0
        temp = 0
        for r in range(k):
            if s[r] in vowel:
                temp += 1
        count = max(temp,count)
        while l <= len(s)-k and r < len(s)-1:
            r += 1
            if s[r] in vowel:
                temp += 1
            if s[l] in vowel:
                temp -= 1
            l +=1
            count = max(temp,count)
        
        return count


        