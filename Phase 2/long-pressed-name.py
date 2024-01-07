class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        diff = 0
        if name[0] != typed[0]:
            return False
        i = 0
        j = 0
        flag = True
        ans = ""
        while i < len(name) and j < len(typed):
            if flag:
                if name[i] == typed[j]:
                    i += 1
                    j += 1
                    diff = 0
                else:
                    flag = False
            else:
                if name[i-1] == typed[j]:
                    j += 1
                    diff = 0
                else:
                    diff += 1
                    flag = True
            if diff > 1:
                print("wrong")
                return False
        while j < len(typed):
            if name[i-1] == typed[j]:
                j += 1
            else:
                return False
                    
        
        return i == len(name) and j == len(typed)