# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def inOrder(root):
            if root:
                inOrder(root.left)
                ans.append(root.val)
                inOrder(root.right)
        inOrder(root)
        if len(set(ans)) != len(ans):
            return False
        return ans == sorted(ans)  