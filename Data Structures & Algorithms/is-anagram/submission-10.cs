public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length == 0 || t.Length == 0 || s.Length != t.Length) return false;
        var sCharArray = s.ToCharArray();
        var tCharArray = t.ToCharArray();
        int[] count = new int[26];
        for(int i = 0; i < sCharArray.Length; i++) {
            count[sCharArray[i] - 'a']++;
            count[tCharArray[i] - 'a']--;
        }

        foreach(var c in count) {
            if(c != 0) return false;
        }
        return true;
    }
}
