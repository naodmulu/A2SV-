class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def checker(char,k,s):
            l = 0
            r = 0
            ans = 0
            while l < len(s) and r < len(s):
                if s[r] == char:
                    ans = max(ans,r-l+1)
                    r += 1
                elif s[r] != char and k > 0:
                    ans = max(ans,r-l+1)
                    k -= 1
                    r += 1
                elif s[r] != char and k == 0:
                    if s[l] == char:
                        
                        l += 1
                    else:
                        k += 1
                        l += 1
            return ans
        # print(checker("T",k,answerKey),checker("F",k,answerKey))
        return max(checker("T",k,answerKey),checker("F",k,answerKey))


        