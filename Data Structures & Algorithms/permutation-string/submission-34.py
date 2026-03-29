class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count, window = [0] * 26, [0] * 26

        for i in range(len(s1)):
            count[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += 1 if count[i] == window[i] else 0
        
        l = 0

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            rc = s2[r]
            index = ord(rc) - ord('a')
            window[index] += 1
            if count[index] == window[index]:
                matches += 1
            elif count[index] + 1 == window[index]:
                matches -= 1
            
            lc = s2[l]
            index = ord(lc) - ord('a')
            window[index] -= 1
            if count[index] == window[index]:
                matches += 1
            elif count[index] - 1 == window[index]:
                matches -= 1
            l += 1
        return matches == 26