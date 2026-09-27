# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, shouldBeHigher, showBeLower):
            if not node:
                return True
            
            if (not node.val > shouldBeHigher) or not (node.val < showBeLower):
                return False
            return dfs(node.left, shouldBeHigher, node.val) and dfs(node.right, node.val, showBeLower)
        
        return dfs(root, float('-inf'), float('inf'))