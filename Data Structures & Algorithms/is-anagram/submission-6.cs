public class Solution {
    public bool IsAnagram(string s, string t) {
        var result = true;
        if(s.Count() != t.Count()) {
            return false;
        }
        var distintChars = s.Distinct();
        var distintOposite = t.Distinct();
        foreach (char c in distintChars)
        {
            if (s.Count(x => x == c) != t.Count(x => x == c))
{
    result = false;
}
        }
        return result;
    }
}
