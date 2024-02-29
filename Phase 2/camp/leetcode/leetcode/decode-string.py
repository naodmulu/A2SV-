class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        
        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char == "[":
                stack.append(num)
                stack.append(char)
                num = 0
            elif char == "]":
                output = ""
                while 1:
                    temp = stack.pop()
                    if temp == "[":break
                    output = temp + output
                stack.append(output*stack.pop())
            
            else:
                stack.append(char)
        
        print(stack)
        return "".join(stack)




            




        

        