public class Solution {
    public int LongestConsecutive(int[] nums) {
        var set = new HashSet<int>(nums);
        var res = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (set.Contains(nums[i] - 1)) {
                continue;
            }
            var length = 1;
            while (set.Contains(nums[i] + length)) {
                length++;
            }
            res = Math.Max(res, length);
        }
        return res;
    }
}
