public class Solution {
    public int Trap(int[] height) {
        var len = height.Length;
        if (len == 0) {
            return 0;
        }

        var prefix = new int[len];
        prefix[0] = height[0];
        var suffix = new int[len];
        suffix[len - 1] = height[len - 1];
        for (int i = 1; i < len; i++) {
            prefix[i] = Math.Max(prefix[i - 1], height[i]);
        }
        for (int i = len - 2; i >= 0; i--) {
            suffix[i] = Math.Max(suffix[i + 1], height[i]);
        }
        var res = 0;
        for (int i = 0; i < len; i++) {
            res += Math.Min(prefix[i], suffix[i]) - height[i];
        }
        return res;
    }
}
