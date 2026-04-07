public class Solution {
    public int LongestConsecutive(int[] nums) {
        var set = new HashSet<int>(nums);
        var res = 0;
        foreach (var n in nums) {
            if (set.Contains(n - 1)) {
                continue;
            }
            var length = 1;
            while (set.Contains(n + length)) {
                length++;
            }
            res = Math.Max(res, length);
        }
        return res;
    }
}
