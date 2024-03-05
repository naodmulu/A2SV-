class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        checker = [0,0,["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
        
        if len(digits) == 0:
            return ans

        def helper(idx,pos,path):
            # print(path)
            if len(path) == len(digits):
                ans.append("".join(path))
                return 
        
            for i in range(idx,len(digits)):
                temp = int(digits[i])
                for j in range(len(checker[temp])):
                    path.append(checker[temp][j])
                    helper(i+1,j,path)
                    path.pop()
        
        helper(0,0,[])
        return ans

