# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        diff = 0
        def maxDiff(root,mini,maxi):
            nonlocal diff
            if not root:
                return
            mini = min(mini,root.val)
            maxi = max(maxi,root.val)

            maxDiff(root.left,mini,maxi)
            maxDiff(root.right,mini,maxi)

            diff = max(abs(root.val-mini),abs(root.val-maxi),diff)
        
        maxDiff(root,float("inf"),float("-inf"))
        return diff
