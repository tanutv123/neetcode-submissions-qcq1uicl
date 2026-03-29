# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        nxt = head
        while n:
            nxt = nxt.next
            n -= 1
        
        prev = dummy
        while nxt:
            nxt = nxt.next
            prev = prev.next
        
        prev.next = prev.next.next
        return dummy.next