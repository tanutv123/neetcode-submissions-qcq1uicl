public class Solution {
    public int LengthOfLongestSubstring(string s) {
        int l = 0;
        HashSet<char> cSet = new HashSet<char>();
        int result = 0;
        for(int r = 0; r < s.Length; r++) {
            while(cSet.Contains(s[r])) {
                cSet.Remove(s[l]);
                l += 1;
            }
            cSet.Add(s[r]);
            result = Math.Max(result, r - l + 1);
        }
        return result;
    }
}
