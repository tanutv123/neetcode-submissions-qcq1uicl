public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        var n = nums.Length;
        var prefix = new int[n];
        Array.Fill(prefix, 1);
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }
        var suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            prefix[i] = prefix[i] * suffix;
            suffix = nums[i] * suffix;
        }
        return prefix;
    }
}
