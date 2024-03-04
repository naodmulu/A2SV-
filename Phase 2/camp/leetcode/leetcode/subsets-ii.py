class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        path = []
        def helper(idx,path):
            if len(path) == len(nums):
                
                ans.add(tuple(sorted(path)[:]))
                return 
            
            ans.add(tuple(sorted(path)[:]))
            
            for i in range(idx,len(nums)):
                path.append(nums[i])
                helper(i+1,path)
                path.pop()
        helper(0,path)
        return sorted(ans)
        