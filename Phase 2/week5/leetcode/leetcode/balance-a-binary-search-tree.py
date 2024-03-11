# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inOrder = []
        def traversal(root):
            if root:
                traversal(root.left)
                inOrder.append(root.val)
                traversal(root.right)
        
        def constructor(l,r):
            if l > r:
                return
            mid = (l+r)//2

            return TreeNode(inOrder[mid],constructor(l,mid-1),constructor(mid+1,r))

        traversal(root)
        return constructor(0,len(inOrder)-1)
        