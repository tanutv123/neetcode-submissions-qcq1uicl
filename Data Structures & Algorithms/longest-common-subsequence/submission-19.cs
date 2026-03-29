public class Solution {
    public int LongestCommonSubsequence(string text1, string text2) {
        int N = text1.Length;
        int M = text2.Length;

        int[] dp = new int[M + 1];

        for (int i = 0; i < N; i++) {
            int[] currRow = new int[M + 1];
            for (int j = 0; j < M; j++) {
                if (text1[i] == text2[j]) {
                    currRow[j + 1] = 1 + dp[j];
                } else {
                    currRow[j + 1] = Math.Max(currRow[j], dp[j + 1]);
                }
            }
            dp = currRow; // Move current row to previous row
        }

        return dp[M];
    }
}
