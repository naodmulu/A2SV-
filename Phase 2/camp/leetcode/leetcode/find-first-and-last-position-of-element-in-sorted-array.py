class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        l = bisect_left(nums,target)
        r = bisect_right(nums,target)
        if l != r:
            ans = [l,r-1]
        return ans





        