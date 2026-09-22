# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append([root])
        res = []

        while q:
            arr = q.popleft()
            temp = []
            temp2 = []
            for node in arr:
                temp2.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp and len(temp) > 0:
                q.append(temp)
            res.append(temp2)
        return res
                
                
