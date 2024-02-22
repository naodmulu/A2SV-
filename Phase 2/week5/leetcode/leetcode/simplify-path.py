class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        # print(path)
        for p in path:
            if p == '..' and stack:
                stack.pop()
            elif p != "" and p != "." and p!= "..":
                stack.append(p)
        # print(stack)
        return "/" + "/".join(stack)
        