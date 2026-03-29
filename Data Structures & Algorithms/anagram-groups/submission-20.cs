public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs)
    {
        if (strs.Length == 1) return [[ strs[0] ]];
        var res = new List<List<string>>();
        var visited = new bool[strs.Length];
        for (int i = 0; i < strs.Length; i++)
        {
            if (visited[i]) {
                continue;
            }
            var current = new List<string>();
            current.Add(strs[i]);
            for (int j = i + 1; j < strs.Length; j++)
            {
                if (!visited[j] && IsAnagram(strs[i], strs[j]))
                {
                    current.Add(strs[j]);
                    visited[j] = true;
                }
            }
            res.Add(current);
        }

        return res;
    }


    bool IsAnagram(string s1, string s2)
    {
        if (s1.Length != s2.Length) return false;

        var count = new int[26];

        for(int i = 0; i < s1.Length; i++)
        {
            count[s1[i] - 'a']++;
            count[s2[i] - 'a']--;
        }

        foreach (var entry in count)
        {
            if (entry != 0)
            {
                return false;
            }
        }
        return true;
    }
}
