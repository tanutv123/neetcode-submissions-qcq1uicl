/*
// Definition for a Node.
public class Node {
    public int val;
    public Node next;
    public Node random;
    
    public Node(int _val) {
        val = _val;
        next = null;
        random = null;
    }
}
*/

public class Solution {
    public Node copyRandomList(Node head) {
        Dictionary<Node, Node> oldToCopy = new Dictionary<Node, Node>();
        Node curr = head;

        while(curr != null) {
            oldToCopy[curr] = new Node(curr.val);
            curr = curr.next;
        }

        curr = head;
        while(curr != null) {
            Node copy = oldToCopy[curr];
            copy.random = curr.random != null ? oldToCopy[curr.random] : null;
            copy.next = curr.next != null ? oldToCopy[curr.next] : null; 
            curr = curr.next;
        }
        return head != null ? oldToCopy[head] : null;
    }
}
