class Solution:
    def generateParenthesis(self, k: int) -> List[str]:
        # i and o
        n = 2
        ans = set()
        def isValid(path):
            path = "".join(path)
            stack = []
            for i in range(len(path)):
                if stack and stack[-1] == "(" and path[i] == ")":
                    stack.pop()
                else:
                    stack.append(path[i])

            return len(stack) == 0
        def helper(idx,path):

            if len(path) == k:
                if isValid(path):
                    ans.add("".join(path[:]))
                return

            for i in range(idx,k):
                path.append("((")
                helper(i+1,path)
                path.pop()

                path.append("))")
                helper(i+1,path)
                path.pop()

                path.append("()")
                helper(i+1,path)
                path.pop()

                path.append(")(")
                helper(i+1,path)
                path.pop()
            
        helper(0,[])
        return ans
