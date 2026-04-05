public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        var prefix = new int[nums.Length];
        prefix[0] = 1;
        for (int i = 1; i < nums.Length; i++) {
            prefix[i] = nums[i - 1] * prefix[i - 1];
        }
        var postfix = 1;
        for (int i = nums.Length - 1; i >= 0; i--) {
            prefix[i] *= postfix;
            postfix *= nums[i];
        }
        return prefix;
    }
}
