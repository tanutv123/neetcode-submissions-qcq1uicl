public class Solution
{
    public int Trap(int[] height)
    {
        if (height.Length == 0)
        {
            return 0;
        }
        var res = 0;
        var l = 0;
        var r = height.Length - 1;
        var maxL = height[l];
        var maxR = height[r];
        while (l < r)
        {
            if (maxL < maxR)
            {
                l++;
                maxL = Math.Max(maxL, height[l]);
                res += maxL - height[l];
            }
            else
            {
                r--;
                maxR = Math.Max(maxR, height[r]);
                res += maxR - height[r];
            }
        }
        return res;
    }
}
