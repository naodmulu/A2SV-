# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def smallest(root,k):
            if len(ans) == k:
                return
            if root:
                smallest(root.left,k)
                if len(ans) < k:
                    ans.append(root.val)
                smallest(root.right,k) 
        smallest(root,k)
        return ans[-1]






        