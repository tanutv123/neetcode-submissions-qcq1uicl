public class Solution {
    public bool IsInterleave(string s1, string s2, string s3) {
        int r = s1.Length, c = s2.Length;
        if(r + c != s3.Length) {
            return false;
        }
        bool[,] dp = new bool[r+1,c+1];
        dp[r,c] = true;
    
        for(int i = r; i >= 0; i--) {
            for(int j = c; j >= 0; j--) {
                if (i < r && s1[i] == s3[i+j] && dp[i+1,j]) {
                    dp[i,j] = true;
                }
                if (j < c && s2[j] == s3[i+j] && dp[i,j+1]) {
                    dp[i,j] = true;
                }
            }
        }
        return dp[0,0];
    }
}
