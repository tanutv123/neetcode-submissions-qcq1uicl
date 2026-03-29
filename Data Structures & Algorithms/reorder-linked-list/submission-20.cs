/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

public class Solution {
    public void ReorderList(ListNode head) {
        var slow = head;
        var fast = head.next;

        while(fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        var curr = slow.next;
        var prev = slow.next = null;
        while(curr != null) {
            var temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }

        ListNode first = head;
        ListNode second = prev;
        while (second != null) {
            var tmp1 = first.next;
            var tmp2 = second.next;
            first.next = second;
            second.next = tmp1;
            first = tmp1;
            second = tmp2;
        }
    }
}
