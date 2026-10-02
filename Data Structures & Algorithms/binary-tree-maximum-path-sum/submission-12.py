# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        currMax = float('-inf')
        def dfs(root):
            if not root:
                return 0

            
            left = dfs(root.left)
            right = dfs(root.right)
            total = root.val
            if left > 0:
                total += left
            if right > 0:
                total += right
            nonlocal currMax
            currMax = max(currMax, total)
            return root.val + max(left if left > 0 else 0, right if right > 0 else 0)
        
        dfs(root)
        return currMax