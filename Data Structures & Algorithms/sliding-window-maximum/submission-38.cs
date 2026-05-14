public class Solution {
    public int[] MaxSlidingWindow(int[] nums, int k) {
        var deque = new LinkedList<int>();
        var l = 0;
        var r = 0;
        var res = new int[nums.Length - k + 1];
        while (r < nums.Length) {
            while (deque.Count > 0 && nums[deque.Last()] < nums[r]) {
                deque.RemoveLast();
            }
            deque.AddLast(r);
            if (l > deque.First()) {
                deque.RemoveFirst();
            }
            if (r + 1 >= k) {
                res[l] = nums[deque.First()];
                l++;
            }
            r++;
        }
        return res;
    }
}
