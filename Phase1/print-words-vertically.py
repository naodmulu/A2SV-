class Solution:
    def printVertically(self, s: str) -> List[str]:
        slist = s.split()
        lenmax = 0
        for i in range(len(slist)):
            lenmax = max(lenmax,len(slist[i])) 
        ans = []
        for i in range(lenmax):
            column = ''
            for word in slist:
                if i < len(word):
                    column += word[i]
                else:
                    column += ' '
            ans.append(column.rstrip())

        return ans

            
        