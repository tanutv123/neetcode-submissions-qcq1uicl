public class Solution
{
    public int LongestCommonSubsequence(string text1, string text2)
    {
        Dictionary<string, int> cache = new Dictionary<string, int>();
        return Dfs(text1, text2, 0, 0, cache);
    }

    public int Dfs(string text1, string text2, int i, int j, Dictionary<string, int> cache)
    {
        if (i == text1.Length || j == text2.Length)
        {
            return 0;
        }

        var stringKey = $"{i},{j}";

        if (cache.ContainsKey(stringKey))
        {
            return cache[stringKey];
        }

        if (text1[i] == text2[j])
        {
            cache[stringKey] = 1 + Dfs(text1, text2, i + 1, j + 1, cache);
            return cache[stringKey];
        }
        else
        {
            cache[stringKey] = Math.Max(Dfs(text1, text2, i + 1, j, cache), Dfs(text1, text2, i, j + 1, cache));
            return cache[stringKey];
        }
    }
}
