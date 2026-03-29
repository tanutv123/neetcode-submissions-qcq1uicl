"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyOfNode = {None: None} # key: realNode.key => value: copy of node
        curr = head
        while curr:
            copyOfNode[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = copyOfNode[curr]
            copy.next = copyOfNode[curr.next] if curr.next else None
            copy.random = copyOfNode[curr.random] if curr.random else None
            curr = curr.next
        return copyOfNode[head]

