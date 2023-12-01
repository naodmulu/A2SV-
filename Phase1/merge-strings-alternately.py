class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        ans =""
        len1 = len(word1)
        len2 = len(word2)
        while len1 or len2:
            print(len1,len2)
            if len1 and len2:
                ans+= word1[-len1] + word2[-len2]
                len1 = len1 -1
                len2 = len2 -1
                
            elif len1 and len2 == 0:
                ans+= word1[-len1]
                len1 -=1
            elif len1 == 0 and len2:
                ans += word2[-len2]
                len2 -=1
            print(len1,len2)
        return ans


        