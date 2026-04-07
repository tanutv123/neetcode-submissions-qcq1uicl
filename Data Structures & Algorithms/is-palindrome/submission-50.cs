public class Solution {
    public bool IsPalindrome(string s) {
        var l = 0;
        var r = s.Length - 1;
        while (l < r) {
            while (l < r && !IsAlphaNum(s[l])) {
                l++;
            }
            while (l < r && !IsAlphaNum(s[r])) {
                r--;
            }
            if (char.ToLower(s[l]) != char.ToLower(s[r])) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
    private bool IsAlphaNum(char c) {
        return ('A' <= c && c <= 'Z') || ('a' <= c && c <= 'z') || ('0' <= c && c <= '9');
    }
}
