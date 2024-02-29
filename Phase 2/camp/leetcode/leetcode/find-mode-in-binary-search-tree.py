# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = {}
        def inOrder(root):
            if root:
                inOrder(root.left)
                if root.val in dic:
                    dic[root.val] += 1
                else:
                    dic[root.val] = 1
                inOrder(root.right)
        inOrder(root)
        ans = []
        li = sorted(dic.items(), key = lambda x:x[1],reverse = True)
        # print(li)
        for key,val in li:
            if val == li[0][1]:
                ans.append(key)
        return ans