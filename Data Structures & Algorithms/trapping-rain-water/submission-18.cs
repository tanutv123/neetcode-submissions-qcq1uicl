public class Solution {
    public int Trap(int[] height) {
        var length = height.Length;
        if (length == 0) {
            return 0;
        }
        var prefix = new int[length];
        prefix[0] = height[0];
        var suffix = new int[length];
        suffix[length - 1] = height[length - 1];

        for (int i = 1; i < length; i++) {
            prefix[i] = Math.Max(prefix[i - 1], height[i]);
        }

        for (int i = length - 2; i >= 0; i--) {
            suffix[i] = Math.Max(suffix[i + 1], height[i]);
        }

        var res = 0;
        for (int i = 0; i < length; i++) {
            res += Math.Min(prefix[i], suffix[i]) - height[i];
        }
        return res;
    }
}
