public class Solution {
    public int CharacterReplacement(string s, int k) {
        var count = new Dictionary<char, int>();
        var maxF = 0;
        int l = 0;
        var res = 0;
        for(var r = 0; r < s.Length; r++) {
            var c = s[r];
            if (count.ContainsKey(s[r])) {
                count[s[r]]++;
            } else {
                count[s[r]] = 1;
            }
            maxF = Math.Max(count[c], maxF);
            while ((r - l + 1) - maxF > k) {
                count[s[l]]--;
                l++;
            }
            res = Math.Max(res, r - l + 1);
        }
        return res;
    }
}
