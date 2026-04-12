public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var dict = new Dictionary<string, List<string>>();

        foreach (var str in strs) {
            var count = new int[26];
            foreach (var c in str) {
                count[c - 'a']++;
            }
            var key = string.Join(",", count);
            if (!dict.ContainsKey(key)) {
                dict[key] = new List<string>();
            }
            dict[key].Add(str);
        }
        return dict.Values.ToList();
    }
}
