class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        
        candidates.sort()
        
        def helper(idx,path,total):
            # print(path,total)
            if total == target:
                ans.add(tuple(path))
                return 
            if total > target:
                return 
            
            for i in range(idx,len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                total += candidates[i]
                helper(i+1,path,total)
                path.pop()
                total -= candidates[i]


        helper(0,[],0)
        return ans
        