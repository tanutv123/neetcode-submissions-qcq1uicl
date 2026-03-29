public class Solution {
    public bool CheckInclusion(string s1, string s2) {
        if(s1.Length > s2.Length) {
            return false;
        }

        int[] count1 = new int[26];
        int[] count2 = new int[26];

        // Initialize character frequency for s1 and first window of s2
        for(int i = 0; i < s1.Length; i++) {
            count1[s1[i] - 'a'] += 1;
            count2[s2[i] - 'a'] += 1;
        }

        int matches = 0;
        for(int i = 0; i < 26; i++) {
            if(count1[i] == count2[i]) {
                matches += 1;
            }
        }

        int l = 0;
        for(int r = s1.Length; r < s2.Length; r++) {
            if(matches == 26) {
                return true;
            }

            // Add new character from the right end
            int indexR = s2[r] - 'a';
            count2[indexR] += 1;
            if(count1[indexR] == count2[indexR]) {
                matches += 1;
            } else if(count1[indexR] + 1 == count2[indexR]) {
                matches -= 1;
            }

            // Remove old character from the left end
            int indexL = s2[l] - 'a';
            count2[indexL] -= 1;
            if(count1[indexL] == count2[indexL]) {
                matches += 1;
            } else if(count1[indexL] - 1 == count2[indexL]) {
                matches -= 1;
            }
            l += 1;
        }

        return matches == 26;
    }
}
