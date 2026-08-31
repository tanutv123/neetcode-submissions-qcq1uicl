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
        dict = {}
        curr = head
        while curr:
            dict[curr] = Node(curr.val)
            curr = curr.next
        
        dummy = Node(0)
        curr = dummy
        while head:
            temp = curr
            curr.next = dict[head]
            curr.next.next = dict[head.next] if head.next else None
            curr.next.random = dict[head.random] if head.random else None
            head = head.next
            curr = curr.next
        return dummy.next