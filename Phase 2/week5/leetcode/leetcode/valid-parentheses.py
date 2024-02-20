class Solution:
    def isValid(self, s: str) -> bool:
        relation = {")":"(", "]":"[", "}":"{"}
        
        stack = [] 
        for i in s:
            if i not in relation:
                stack.append(i)
            elif i in relation:
                if stack == [] or relation[i] != stack.pop():
                    return False
                    break
        else:
            if stack == []:
                return True
            else:
                return False 
            
