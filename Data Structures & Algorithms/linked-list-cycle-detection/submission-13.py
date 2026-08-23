# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        store = set()
        current = head
        while current and current.next:
            if current in store:
                return True
            store.add(current)
            current = current.next
        return False