public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        var prefix = new int[nums.Length];
        prefix[0] = 1;
        var suffix = new int[nums.Length];
        suffix[nums.Length - 1] = 1;

        for (int i = 1; i < nums.Length; i++)
        {
            prefix[i] = nums[i - 1] * prefix[i - 1];
        }

        for (int i = nums.Length - 2; i >= 0; i--)
        {
            suffix[i] = nums[i + 1] * suffix[i + 1];
        }

        for (int i = 0; i < nums.Length; i++)
        {
            prefix[i] = prefix[i] * suffix[i];
        }

        return prefix;
    }
}
