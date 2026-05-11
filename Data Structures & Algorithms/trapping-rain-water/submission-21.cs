public class Solution {
    public int Trap(int[] height) {
        var len = height.Length;
        var l = 0;
        var r = len - 1;
        var maxL = height[l];
        var maxR = height[r];
        var res = 0;
        while (l < r) {
            if (maxL < maxR) {
                l++;
                maxL = Math.Max(maxL, height[l]);
                res += maxL - height[l];
            }
            else {
                r--;
                maxR = Math.Max(maxR, height[r]);
                res += maxR - height[r];
            }
        }
        return res;
    }
}
