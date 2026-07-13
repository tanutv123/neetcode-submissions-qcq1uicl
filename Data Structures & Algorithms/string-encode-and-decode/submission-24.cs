public class Solution
{
    public string Encode(IList<string> strs)
    {
        var res = string.Empty;
        foreach (var s in strs)
        {
            res += s.Length + "#" + s;
        }
        return res;
    }

    public List<string> Decode(string s)
    {
        var res = new List<string>();
        var l = 0;
        var r = 0;
        while (r < s.Length)
        {
            if (s[r] != '#')
            {
                r++;
                continue;
            }
            var n = int.Parse(s[l..r]);
            l = r + 1;
            r = l + n;
            res.Add(s[l..r]);
            l = r;
        }
        return res;
    }
    //5#Hello5#World
}