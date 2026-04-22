public class Solution {
    public int MaxProfit(int[] prices) {
        var res = 0;
        var l = 0;
        var r = 1;
        while (r < prices.Length) {
            var profit = prices[r] - prices[l];
            if (profit < 0) {
                l = r;
            } else {
                res = Math.Max(res, profit);
            }
            r++;
        }
        return res;
    }
}
