public class Solution {
    public string Encode(IList<string> strs)
    {
        var res = new List<string>();

        foreach ( var str in strs )
        {
            res.Add(str.Length + "#" + str);
        }
        return string.Join("", res);
    }
    public List<string> Decode(string s)
    {
        var res = new List<string>();
        for (int i = 0; i < s.Length; i++)
        {
            var j = i + 1;
            while (s[j] != '#')
            {
                j++;
            }
            var check = int.TryParse(s[i..j], out var number);
            var end = j + number;
            var current = s[(j + 1)..(end + 1)];
            res.Add(current);
            i = j + number;
        }
        return res;
    }
}
