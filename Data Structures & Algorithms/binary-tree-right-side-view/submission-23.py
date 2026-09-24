# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []
        while q:
            qLen = len(q)
            flag = True
            for _ in range(qLen):
                node = q.popleft()
                if not node:
                    continue
                if flag:
                    res.append(node.val)
                    flag = False
                q.append(node.right)
                q.append(node.left)
        return res
