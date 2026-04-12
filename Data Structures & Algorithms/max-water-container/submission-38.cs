public class Solution {
    public int MaxArea(int[] heights)
    {
        var l = 0;
        var r = heights.Length - 1;
        var maxL = heights[l];
        var maxR = heights[r];
        var res = 0;
        while (l < r)
        {
            var area = Math.Min(heights[l], heights[r]) * (r - l);
            res = Math.Max(res, area);
            if (heights[l] > heights[r])
            {

                r--;
            }
            else
            {
                l++;
            }
        }

        return res;
    }
}
