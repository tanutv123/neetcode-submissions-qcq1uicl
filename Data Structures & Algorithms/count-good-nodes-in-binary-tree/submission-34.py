# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(root, currMax):
            if not root:
                return
            nonlocal count
            if root.val >= currMax:
                count += 1
            
            currMax = max(root.val, currMax)
            dfs(root.left, currMax)
            dfs(root.right, currMax)

        dfs(root, -101)
        return count
