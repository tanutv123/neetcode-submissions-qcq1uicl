public class Solution {
    public int MaxProfit(int[] prices) {
        int l = 0, r = 1;
        var res = 0;
        while(r < prices.Length) {
            if(prices[l] < prices[r]) {
                var revenue = prices[r] - prices[l];
                res = Math.Max(res, revenue);
            } else {
                l = r;
            }
            r += 1;
        }
        return res;
    }
}
