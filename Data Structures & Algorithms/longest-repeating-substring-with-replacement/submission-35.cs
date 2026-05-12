public class Solution {
    public int CharacterReplacement(string s, int k) {
        var len = s.Length;
        
        var maxF = 0;
        var l = 0;
        var count = new Dictionary<char, int>();
        var res = 0;
        for (int r = 0; r < len; r++) {
            count[s[r]] = count.GetValueOrDefault(s[r], 0) + 1;
            maxF = Math.Max(maxF, count[s[r]]);
            while (r - l + 1 - maxF > k) {
                count[s[l]]--;
                l++;
            }
            res = Math.Max(res, r - l + 1);
        }
        return res;
    }
}
