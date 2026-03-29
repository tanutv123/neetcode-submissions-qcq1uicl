public class Solution {
    public int MaxProfit(int[] prices) {
        int l = 0, r = 1;
        int maxProfit = 0;
        while (r < prices.Length) {
            if(prices[l] < prices[r]) {
                maxProfit = Math.Max(maxProfit, prices[r] - prices[l]);
            } else {
                l = r;
            }
            r += 1;
        }
        return maxProfit;
    }
}
