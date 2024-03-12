# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic = defaultdict(list)
        ans = 0

        def helper(root,pos,l):
            if root:
                dic[l].append(pos)
                helper(root.left,2*pos,l+1)
                helper(root.right,2*pos+1,l+1)

        helper(root,1,0)
        # print(dic)
        for value in dic.values():
            ans= max(ans, max(value)- min(value))

        return ans +1
        