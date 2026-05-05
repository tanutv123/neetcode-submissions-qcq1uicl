public class Solution {
    public int MaxArea(int[] heights) {
        var len = heights.Length;
        var res = 0;
        var l = 0;
        var r = len - 1;
        var maxL = heights[l];
        var maxR = heights[r];

        while (l < r) {
            var area = Math.Min(maxL, maxR) * (r - l);
            res = Math.Max(res, area);
            if (maxL < maxR) {
                l++;
                maxL = Math.Max(maxL, heights[l]);
            } else {
                r--;
                maxR = Math.Max(maxR, heights[r]);
            }
        }
        return res;
    }
}
