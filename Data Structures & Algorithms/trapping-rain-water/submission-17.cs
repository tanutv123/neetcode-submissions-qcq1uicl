public class Solution {
    public int Trap(int[] heights) {
        if(heights == null || heights.Length == 0) {
            return 0;
        }

        int l = 0, r = heights.Length - 1;
        int maxL = heights[l], maxR = heights[r];
        var res = 0;
        while(l < r) {
            if(maxL < maxR) {
                l += 1;
                maxL = Math.Max(heights[l], maxL);
                res += maxL - heights[l];
            } else {
                r -= 1;
                maxR = Math.Max(heights[r], maxR);
                res += maxR - heights[r];
            }
        }
        return res;
    }
}
