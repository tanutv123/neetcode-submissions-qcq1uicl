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
        copy = {None : None}
        curr = head
        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next
        
        curr1 = head
        while curr1:
            copy[curr1].next = copy[curr1.next] if curr1.next else None
            copy[curr1].random = copy[curr1.random] if curr1.random else None
            curr1 = curr1.next

        return copy[head]