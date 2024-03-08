class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def checker(string):
            count = Counter(string)
            for key in count:
                if ord(key) >= 97:
                    if chr(ord(key)-32) not in count:
                        return False
                else:
                    if chr(ord(key)+32) not in count:
                        return False       
            return True
        ans = []
        max_length = 0
        for i in range(len(s)):
            string = ""
            for j in range(i,len(s)):
                string += s[j]
                print(string,ans)
                if len(string) > 1 and len(string) >= max_length and checker(string):
                    max_length = len(string)
                    ans.append(string)
        if max_length == 0:
            return ""
        for i in ans:
            if len(i) == max_length:
                return i
