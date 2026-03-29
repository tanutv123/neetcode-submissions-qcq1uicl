public class Solution {
    public int Change(int amount, int[] coins) {
        Array.Sort(coins);
        int[] dp = new int[amount + 1];
        dp[0] = 1;

        for(int i = coins.Length - 1; i >= 0; i--) {
            int[] nextDp = new int[amount + 1];
            nextDp[0] = 1;

            for(int a = 1; a <= amount; a++) {
                if (a - coins[i] >= 0) {
                    nextDp[a] = nextDp[a - coins[i]] + dp[a];
                }
            }
            dp = nextDp;
        }
        return dp[amount];
    }
}
