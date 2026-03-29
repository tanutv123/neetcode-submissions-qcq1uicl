public class Solution {
    public int CharacterReplacement(string s, int k) {
        int maxF = 0;
        int res = 0;
        Dictionary<char, int> count = new 
                            Dictionary<char, int>();
        int l = 0;

        for(int r = 0; r < s.Length; r++) {
            if(!count.ContainsKey(s[r])) {
                count[s[r]] = 1;
            } else {
                count[s[r]] += 1;
            }

            maxF = Math.Max(maxF, count[s[r]]);
            while (r - l + 1 - maxF > k) {
                count[s[l]] -= 1;
                l += 1;
            }
            res = Math.Max(res, r - l + 1);
        }
        return res;
    }
}
