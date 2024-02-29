# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = {}
        def zigzag(root,l):
            if root:
                zigzag(root.left,l+1)
                if l in dic:
                    dic[l].append(root.val)
                else:
                    dic[l] = [root.val]
                zigzag(root.right,l+1) 
        zigzag(root,0)
        # print(dic)
        ans = []
        for i in range(len(dic)):
            if i%2:
                ans.append(dic[i][::-1])
            else:
                ans.append(dic[i])
        return ans

        