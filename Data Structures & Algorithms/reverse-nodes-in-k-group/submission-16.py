# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                return dummy.next
            prev = self.reverse(groupPrev.next, kth.next)

            temp = groupPrev.next
            groupPrev.next = prev
            groupPrev = temp

    def reverse(self, node, next):
        prev = next
        curr = node

        while curr != next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def getKth(self, node, k):
        while node and k:
            node = node.next
            k -= 1
        return node