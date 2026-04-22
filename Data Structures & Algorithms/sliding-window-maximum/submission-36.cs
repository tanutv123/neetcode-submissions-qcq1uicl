public class Solution {
    public int[] MaxSlidingWindow(int[] nums, int k) {
        var q = new LinkedList<int>();
        var res = new int[nums.Length - k + 1];
        var l = 0;
        var r = 0;
        while (r < nums.Length) {
            while (q.Count > 0 && nums[q.Last.Value] < nums[r]) {
                q.RemoveLast();
            }
            q.AddLast(r);

            if (l > q.First.Value) {
                q.RemoveFirst();
            }

            if (r + 1 >= k) {
                res[l] = nums[q.First.Value];
                l++;
            }
            r++;
        }
        return res;
    }
}
