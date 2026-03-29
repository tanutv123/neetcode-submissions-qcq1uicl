public class KthLargest {
    PriorityQueue<int, int> heap = new PriorityQueue<int, int>();
    int kth = 0;
    public KthLargest(int k, int[] nums) {
        kth = k;
        foreach(var n in nums) {
            heap.Enqueue(n, n);
        }
        while(heap.Count > k) {
            heap.Dequeue();
        }
    }
    
    public int Add(int val) {
        heap.Enqueue(val, val);
        int res = 0;
        while(heap.Count > kth) {
            heap.Dequeue();
        }
        return heap.Peek();
    }
}
