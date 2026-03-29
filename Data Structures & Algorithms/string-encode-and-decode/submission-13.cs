public class Solution {

    public string Encode(IList<string> strs) {
        var result = "";
        foreach(var s in strs) {
            int length = s.Length;
            result += length + "#" + s;
        }
        return result;
    }

    public List<string> Decode(string s) {
        var result = new List<string>();
        int i = 0;
    
        while(i < s.Length) {
            int j = i;
            while (s[j] != '#') {
                j += 1;
            }

            var length = int.Parse(s.Substring(i, j - i));
            i = j + 1;
            j = i + length;
            result.Add(s.Substring(i, length));
            i = j;
        }
        return result;
   }
}
