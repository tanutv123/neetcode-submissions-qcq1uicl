public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length != t.Length) {
            return false;
        }
        int[] count = new int[26];
        for(int i = 0; i < s.Length; i++) {
            count[s[i] - 'a'] += 1;
            count[t[i] - 'a'] -= 1;
        }

        foreach(var c in count){
            if (c != 0) {
                return false;
            }
        }
        return true;
    }
}
