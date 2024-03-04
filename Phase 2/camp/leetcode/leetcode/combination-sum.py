class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        path = []
        def helper(idx,path):
            if sum(path) == target:
                ans.add(tuple(path[:]))
                return 
            if sum(path) > target:
                return
            
            for i in range(idx,len(candidates)):
                path.append(candidates[i])
                while 1:
                    helper(i,path)
                    break
                helper(i+1,path)
                path.pop()
        helper(0,path)
        return ans