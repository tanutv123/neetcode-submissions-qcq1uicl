public class Solution {
    public int LengthOfLongestSubstring(string s) {
        var res = new HashSet<char>();
        int l = 0;
        var result = 0;
        for(var r = 0; r < s.Length; r++) {
            while(res.Contains(s[r])) {
                res.Remove(s[l]);
                l += 1;
            }
            res.Add(s[r]);
            result = Math.Max(result, r - l + 1);
        }
        return result;
    }
}
