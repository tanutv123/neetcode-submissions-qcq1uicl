"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
        if not root:
            return None
        clone = {}

        def dfs(node):
            if node in clone:
                return clone[node]
            copy = Node(node.val)
            clone[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        dfs(root)
        return clone[root]