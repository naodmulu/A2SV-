class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        occur = set()
        def helper(idx,path):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for i in range(len(nums)):
                if i in occur:
                    continue
                path.append(nums[i])
                occur.add(i)
                helper(i+1,path)
                path.pop()
                occur.remove(i)
        helper(0,[])
        return ans
        