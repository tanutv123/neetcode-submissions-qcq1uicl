# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        index = 0
        res = -1
        
        def dfs(root):
            if not root:
                return
            nonlocal res, k
            dfs(root.left)
            k -= 1
            if not k:
                res = root.val
            dfs(root.right)
        dfs(root)
        return res

