# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        elif (root.left and not root.right) or (not root.left and root.right):
            return False
        ansl = []
        ansr = []
        def helper(root,side):
            if not root:
                if side:
                    ansr.append("X")
                else:
                    ansl.append("X")
                return
            if side:
                ansr.append(root.val)
                helper(root.left,side)
                helper(root.right,side)
            else:
                ansl.append(root.val)
                helper(root.right,side)
                helper(root.left,side)
        helper(root.left,True)
        helper(root.right,False)
        # print(ansl,ansr)
        return ansl == ansr