public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var res = new Dictionary<string, List<string>>();

        foreach(var s in strs) {
            int[] count = new int[26];
            for(int i = 0; i < s.Length; i++) {
                count[s[i] - 'a']++;
            }
            var resultKey = string.Join(",", count);
            if(!res.ContainsKey(resultKey)) {
                res[resultKey] = new List<string>();
            }
            res[resultKey].Add(s);
        }
        return res.Values.ToList<List<string>>();
    }
}
