# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, currMax):
            if not root:
                return 0
            res = 1 if root.val >= currMax else 0
            currMax = max(root.val, currMax)
            left = dfs(root.left, currMax)
            right = dfs(root.right, currMax)
            return res + left + right
        return dfs(root, float('-inf'))
