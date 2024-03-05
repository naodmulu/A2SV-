class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = set()
        candidates = range(1,10)
        target = n
        def helper(idx,path,total):
            # print(path,total)
            if total == target:
                if len(path) == k:
                    ans.add(tuple(path))
                    return 
            if total > target:
                return 
            
            for i in range(idx,len(candidates)):
                print(path,idx)
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                total += candidates[i]
                helper(i+1,path,total)
                path.pop()
                total -= candidates[i]


        helper(0,[],0)
        return ans
        