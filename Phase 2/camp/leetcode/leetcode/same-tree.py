# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans = True
        def same(l,r):
            print(r,l)
            if not r and not l:
                return True
            if r and not l:
                return False
            if not r and l:
                return False
            if r and l:
                if r.val == l.val:
                    ans = (same(r.left,l.left)) and (same(r.right,l.right))
                    return ans
                if r.val != l.val:
                    return False
            return ans
        return same(p,q)
        