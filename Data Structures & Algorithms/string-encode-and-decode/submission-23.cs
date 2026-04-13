public class Solution {

    public string Encode(IList<string> strs) {
        var res = string.Empty;

        foreach (var s in strs) {
            res += s.Length + "#" + s;
        }
        return res;
    }

    public List<string> Decode(string s) {
        var res = new List<string>();
        int i = 0;
        while (i < s.Length) {
            var j = i;
            while (s[j] != '#') {
                j++;
            }
            var n = int.Parse(s[i..j]);
            i = j + 1;
            j = j + n + 1;
            res.Add(s[i..j]);
            i = j;
        }
        return res;
    }
}
