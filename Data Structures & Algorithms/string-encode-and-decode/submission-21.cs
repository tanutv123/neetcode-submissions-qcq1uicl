public class Solution {

    public string Encode(IList<string> strs) {
        var res = string.Empty;
        foreach (var str in strs) {
            res += str.Length + "#" + str;
        }
        return res;
    }

    public List<string> Decode(string s)
    {
        var res = new List<string>();
        var i = 0;
        while (i < s.Length)
        {
            var j = i;
            while (s[j] != '#')
            {
                j++;
            }
            var n = int.Parse(s[i..j]);
            i = j + 1;
            j = i + n;
            res.Add(s[i..j]);
            i = j;
        }
        return res;
    }
}
