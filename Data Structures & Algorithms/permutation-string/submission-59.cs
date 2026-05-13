public class Solution {
    public bool CheckInclusion(string s1, string s2) {
        if (s1.Length > s2.Length) {
            return false;
        }
        var count1 = new int[26];
        var count2 = new int[26];

        for (int i = 0; i < s1.Length; i++) {
            count1[s1[i] - 'a']++;
            count2[s2[i] - 'a']++;
        }

        var matches = 0;
        for (int i = 0; i < 26; i++) {
            if (count1[i] == count2[i]) {
                matches++;
            }
        }
        var l = 0;
        for (int r = s1.Length; r < s2.Length; r++) {
            if (matches == 26) {
                return true;
            }

            var index = s2[r] - 'a';
            count2[index]++;
            if (count2[index] == count1[index]) {
                matches++;
            } else if (count2[index] == count1[index] + 1) {
                matches--;
            }

            index = s2[l] - 'a';
            count2[index]--;
            l++;
            if (count2[index] == count1[index]) {
                matches++;
            } else if (count2[index] == count1[index] - 1) {
                matches--;
            }
        }
        return matches == 26;
    }
}
