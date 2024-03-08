# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(l,r):
            new = nums[l:r]
            if new:
                temp = max(new)
                i = nums.index(temp)

                return TreeNode(temp,helper(l,i),helper(i+1,r))
        return helper(0,len(nums))