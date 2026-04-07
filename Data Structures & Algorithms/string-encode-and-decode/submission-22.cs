public class Solution {

    public string Encode(IList<string> strs) {
        var res = string.Empty;
        foreach (var str in strs) {
            res += str.Length + "#" + str;
        }
        return res;
    }

    public List<string> Decode(string s) {
        var res = new List<string>();
        //5#Hello5#World
        for (int i = 0; i < s.Length; i++) {
            var j = i;
            while (s[j] != '#') {
                j++;
            }
            var number = int.Parse(s[i..j]);
            i = j + 1;
            j = i + number;
            res.Add(s[i..j]);
            i = j - 1;
        }
        return res;
    }
}
