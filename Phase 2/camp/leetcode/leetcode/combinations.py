class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def helper(idx,path):
            if len(path) == k:
                ans.append(path[:])
                return 
            if idx > n:
                return 
            
            for i in range(idx,n+1):
                path.append(i)
                helper(i+1,path)
                path.pop()
        helper(1,path)
        return ans
