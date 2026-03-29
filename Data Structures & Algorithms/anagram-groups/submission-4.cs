public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var res = new Dictionary<string, List<string>>();
        foreach(var s in strs) {
            var count = new int[26];
            var charArray = s.ToCharArray();
            foreach(var c in charArray) {
                count[c - 'a']++;
                // c = a which is 97 => a - a = 97 - 97 = 0
                //count[0] = 1
            }
            var resultKey = string.Join(',', count);
            if(!res.ContainsKey(resultKey)) {
                res[resultKey] = new List<string>();
            }
            res[resultKey].Add(s);
        }      
        return res.Values.ToList<List<string>>();
    }
}