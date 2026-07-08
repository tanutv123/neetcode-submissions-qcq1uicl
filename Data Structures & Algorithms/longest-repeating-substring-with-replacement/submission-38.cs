public class Solution {
    public int CharacterReplacement(string s, int k) {
        var res = 0;
        var mostFreq = 0;
        var dict = new Dictionary<char, int>();
        var l = 0;
        var r = 0;
        for (r = 0; r < s.Length; r++) {
            dict[s[r]] = dict.GetValueOrDefault(s[r], 0) + 1;
            mostFreq = Math.Max(mostFreq, dict[s[r]]);
            while ((r - l + 1) - mostFreq > k) {
                dict[s[l]]--;
                l++;
            }
            res = Math.Max(res, r - l + 1);
        }
        return res;
    }
}
