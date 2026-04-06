public class Solution {
    public bool IsPalindrome(string s) {
        var l = 0;
        var r = s.Length - 1;
        while (l <= r) {
            while (!IsAlphaNumericCharacter(s[l]) && l < s.Length - 1) {
                l++;
            }
            while (!IsAlphaNumericCharacter(s[r]) && r > 0) {
                r--;
            }
            if (l <= r && s[l].ToString().ToLower() != s[r].ToString().ToLower()) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }

    private bool IsAlphaNumericCharacter(char c) {
        return ('A' <= c  && c <= 'Z') || ('a' <= c  && c <= 'z') || ('0' <= c  && c <= '9');
    }
}
