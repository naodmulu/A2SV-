class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for b in s:
            if b == "(":
                stack.append(b)
            else:
                score = 0
                while 1:
                    temp = stack.pop()
                    if temp == "(":
                        break
                    else:
                        score += temp
                if score == 0:
                    stack.append(1)
                else:
                    stack.append(2*score)
        return sum(stack)
