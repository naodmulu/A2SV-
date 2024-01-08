class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        checker = Counter(p)
        ans = []
        i = 0
        j = 0
        while i < len(s) and j < len(s):
            # print(i,j)
            if s[i] not in checker:
                i += 1
                j += 1
            else:
                if s[j] in checker and checker[s[j]] > 0:
                    if j-i+1 == len(p):
                        ans.append(i)
                    checker[s[j]] -= 1
                    j += 1
                else:
                    checker[s[i]] += 1
                    i += 1
            

        return ans

        # time complexity = O(s+p)
        #space = O(1)




        