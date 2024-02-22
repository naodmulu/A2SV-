class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # print(6//-132)
        for t in tokens:
            # print(stack)
            if t == "+":
                s = stack.pop()
                f = stack.pop()
                stack.append(f+s)
            elif t == "-":
                s = stack.pop()
                f = stack.pop()
                stack.append(f-s)
                
            elif t == "*":
                s = stack.pop()
                f = stack.pop()
                stack.append(f*s)
            elif t == "/":
                s = stack.pop()
                f = stack.pop()
                stack.append(int(f/s))
            else:
                stack.append(int(t))
        
        return stack.pop()
        