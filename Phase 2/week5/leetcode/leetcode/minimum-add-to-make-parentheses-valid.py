class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op = 0
        count = 0
        for char in s:
            if char == ")":
                if op:
                    op -= 1
                else:
                    count += 1      
            else:
                op += 1
        return count + op
        