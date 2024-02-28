# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(root,data):
            if not root:
                return root
            if data == root.val:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                trav = root.right
                while trav.left:
                    trav= trav.left
                root.val = trav.val
                root.right = delete(root.right,trav.val)
            elif data < root.val:
                root.left = delete(root.left,data)
            elif data > root.val:
                root.right = delete(root.right,data)
            
            return root
        return delete(root,key)
