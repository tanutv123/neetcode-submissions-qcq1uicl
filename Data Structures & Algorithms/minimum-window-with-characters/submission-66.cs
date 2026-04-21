public class Solution {
    public string MinWindow(string s, string t) {
        var countT = new Dictionary<char, int>();
        foreach (var c in t) {
            countT[c] = countT.GetValueOrDefault(c, 0) + 1;
        }

        var have = 0;
        var need = countT.Count;
        var window = new Dictionary<char, int>();
        var res = new int[2];
        var resLen = -1;
        var l = 0;
        for (int r = 0; r < s.Length; r++) {
            var c = s[r];
            window[c] = window.GetValueOrDefault(c, 0) + 1;
            if (countT.ContainsKey(c) && countT[c] == window[c]) {
                have++;
            }

            while (have == need) {
                if (resLen == -1 || r - l + 1 < resLen) {
                    res = [l, r];
                    resLen = r - l + 1;
                }
                c = s[l];
                window[c]--;
                if (countT.ContainsKey(c) && countT[c] > window[c]) {
                    have--;
                }
                l++;
            }
        }
        return resLen != -1 ? s[res[0]..(res[1] + 1)] : string.Empty;
    }
}
