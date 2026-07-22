public class Solution {
    public int LongestConsecutive(int[] nums) {
        var res = 0;
        var set = new HashSet<int>(nums);
        for (int i = 0; i < nums.Length; i++) {
            var length = 1;
            while (set.Contains(nums[i] + length)) {
                length++;
            }
            res = Math.Max(res, length);
        }
        return res;
    }
}
