# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        res = None
        def dfs(root, left, right):
            nonlocal res
            if not root:
                return [left, right]
            arr1 = dfs(root.left, left, right)
            arr2 = dfs(root.right, left, right)
            if root == p:
                left = True
            if root == q:
                right = True
            left = left or arr1[0] or arr2[0]
            right = right or arr1[1] or arr2[1]
            if left and right:
                res = root
                left = right = False
                            
            return [left, right]
        dfs(root, False, False)
        return res