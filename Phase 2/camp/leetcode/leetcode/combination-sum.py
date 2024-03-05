class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        path = []
        def helper(idx,path,total):
            if total == target:
                ans.add(tuple(path[:]))
                return 
            if total > target:
                return
            
            for i in range(idx,len(candidates)):
                path.append(candidates[i])
                total += candidates[i]
                helper(i,path,total)
                path.pop()
                total -= candidates[i]
        helper(0,path,0)
        return ans