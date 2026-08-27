# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1 = l2 = head
        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next
        
        prev = None
        curr = l1
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        l1 = head

        while prev.next:
            # if l1 == prev:
            #     break
            temp = l1.next
            temp2 = prev.next
            l1.next = prev
            prev.next = temp
            l1 = temp
            prev = temp2