public class Solution {
    public int MaxArea(int[] heights) {
        var l = 0;
        var r = heights.Length - 1;
        var res = 0;
        while (l < r) {
            var area = Math.Min(heights[l], heights[r]) * (r - l);
            res = Math.Max(res, area);
            if (heights[l] < heights[r]) {
                l++;
            }
            else 
            {
                r--;
            }
        }
        return res;
    }
}
