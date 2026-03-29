public class Solution {
    public bool IsPalindrome(string s) {
        int l = 0;
        int r = s.Length - 1;
        while(l < r) {
            if (l < r && !ValidChar(s[l])) {
                l += 1;
            } else if(l < r && !ValidChar(s[r])) {
                r -= 1;
            } else {
                if (char.ToLower(s[l]) != char.ToLower(s[r])) {
                    return false;
                }
                l += 1;
                r -= 1;
            }
        }
        return true;
    }
    public bool ValidChar(char c) {
        return (c >= 'A' && c <= 'Z' || 
                c >= 'a' && c <= 'z' || 
                c >= '0' && c <= '9');
    }
}
