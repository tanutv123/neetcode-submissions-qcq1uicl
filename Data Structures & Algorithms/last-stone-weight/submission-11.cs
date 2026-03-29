public class Solution {
    public int LastStoneWeight(int[] stones) {
        PriorityQueue<int, int> heap = new PriorityQueue<int, int>();
        foreach(var stone in stones) {
            heap.Enqueue(stone, -stone);
        }

        while(heap.Count > 1) {
            int stone1 = heap.Dequeue();
            int stone2 = heap.Dequeue();
            heap.Enqueue(stone1 - stone2, stone2 - stone1);
        }
        heap.Enqueue(0,0);
        return heap.Peek();
    }
}
