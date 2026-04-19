public class Solution {
    public int CharacterReplacement(string s, int k) {
        var set = new HashSet<char>(s);
        var res = 0;

        foreach (var c in s)
        {
            var count = 0;
            var l = 0;
            for (int r = 0; r < s.Length; r++)
            {
                if (s[r] == c)
                {
                    count += 1;
                }

                while ((r - l + 1) - count > k)
                {
                    if (s[l] == c)
                    {
                        count--;
                    }
                    l += 1;
                }
                res = Math.Max(res, r - l + 1);
            }
        }

        return res;
    }
}
