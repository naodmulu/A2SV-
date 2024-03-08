# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def helper(root,path):
            nonlocal ans
            if not root:
                return
            if not root.left and not root.right:
                path += str(root.val)
                ans += int(path)
            

            path += str(root.val)
            helper(root.left,path)
            helper(root.right,path)

        helper(root,"")
        print(ans)
        return ans