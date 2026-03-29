public class Solution {
    public void ReorderList(ListNode head) {
        if (head == null || head.next == null) return;

        // Step 1: Find the middle of the list
        var slow = head;
        var fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Step 2: Reverse the second half of the list
        var prev = (ListNode)null;
        var curr = slow.next;
        slow.next = null; // Split the list into two halves
        while (curr != null) {
            var temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }

        // Step 3: Merge the two halves
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
