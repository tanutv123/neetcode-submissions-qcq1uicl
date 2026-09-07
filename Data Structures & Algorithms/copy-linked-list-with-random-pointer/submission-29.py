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
        dict = defaultdict(lambda: Node(0))
        dict[None] = None

        curr = head
        while curr:
            copy = dict[curr]
            copy.val = curr.val
            copy.random = dict[curr.random]
            copy.next = dict[curr.next]
            curr = curr.next
        return dict[head]