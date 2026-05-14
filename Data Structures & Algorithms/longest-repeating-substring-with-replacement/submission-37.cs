public class Solution {
    public int CharacterReplacement(string s, int k) {
        var count = new Dictionary<char, int>();
        var l = 0;
        var res = 0;
        var maxF = 0;
        for (int r = 0; r < s.Length; r++) {
            count[s[r]] = count.GetValueOrDefault(s[r], 0) + 1;
            maxF = Math.Max(maxF, count[s[r]]);
            if (r - l + 1 - maxF > k) {
                count[s[l]]--;
                l++;
            }
            res = Math.Max(res, r - l + 1);
        }
        return res;
    }
}
