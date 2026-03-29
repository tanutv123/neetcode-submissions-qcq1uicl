public class Solution {
    public int[] MaxSlidingWindow(int[] nums, int k) {
        int n = nums.Length;
        var q = new LinkedList<int>();
        var res = new List<int>();
        int l = 0, r = 0;
        while(r < n) {
            while(q.Count > 0 && nums[q.Last.Value] < nums[r]) {
                q.RemoveLast();
            }
            q.AddLast(r);

            if(l > q.First.Value) {
                q.RemoveFirst();
            }

            if(r + 1 >= k) {
                res.Add(nums[q.First.Value]);
                l += 1;
            }
            r += 1;
        }
        return res.ToArray();
    }
}
