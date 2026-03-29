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
        copyOfOld = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            copyOfOld[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = copyOfOld[curr]
            copy.next = copyOfOld[curr.next]
            copy.random = copyOfOld[curr.random]
            curr = curr.next
        return copyOfOld[head]