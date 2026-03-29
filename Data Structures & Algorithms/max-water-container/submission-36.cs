public class Solution {
    public int MaxArea(int[] heights) {
        int l = 0;
        int r= heights.Length - 1;
        int maxL = heights[l];
        int maxR = heights[r];
        var res = 0;
        while(l < r) {
            if(maxL < maxR) {
                int total = maxL * (r - l);
                res = Math.Max(res, total);
                l += 1;
                maxL = Math.Max(maxL, heights[l]);
            } else{
                int total = maxR * (r - l);
                res = Math.Max(res, total);
                r -= 1;
                maxR = Math.Max(maxR, heights[r]);
            }
        }
        return res;
    }
}
