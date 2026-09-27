# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxValue):
            if not root:
                return 0
            
            res = 1 if root.val >= maxValue else 0
            left = dfs(root.left, max(root.val, maxValue))
            right = dfs(root.right, max(root.val, maxValue))
            return res + left + right
        return dfs(root, float('-inf'))
