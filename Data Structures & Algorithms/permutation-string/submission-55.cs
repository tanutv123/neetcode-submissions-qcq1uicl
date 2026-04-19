public class Solution {
    public bool CheckInclusion(string s1, string s2) {
        if (s1.Length > s2.Length) return false;
        var count1 = new int[26];
        var count2 = new int[26];
        for (int i = 0; i < s1.Length; i++) {
            count1[s1[i] - 'a']++;
            count2[s2[i] - 'a']++;
        }

        var l = 0;
        var r = s1.Length - 1;
        while (r < s2.Length) {
            if (string.Join(",", count1) == string.Join(",", count2)) {
                return true;
            }
            count2[s2[l] - 'a']--;
            l++;
            r++;
            if (r < s2.Length) 
            {
                count2[s2[r] - 'a']++;
            }
        }
        return false;
    }
}
