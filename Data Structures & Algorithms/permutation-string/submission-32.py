class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = {chr(i + 97): 0 for i in range(26)}
        count2 = {chr(i + 97): 0 for i in range(26)}

        for i in range(len(s1)):
            c1 = s1[i]
            c2 = s2[i]
            count1[c1] = 1 + count1.get(c1, 0)
            count2[c2] = 1 + count2.get(c2, 0)
        
        matches = 0

        for i in range(26):
            c = chr(i + 97)
            matches += 1 if count1.get(c, 0) == count2.get(c, 0) else 0
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            c2 = s2[r]
            count2[c2] = 1 + count2.get(c2, 0)
            if c2 in count1 and count1[c2] == count2[c2]:
                matches += 1
            elif count1[c2] + 1 == count2[c2]:
                matches -= 1
            
            
            c1 = s2[l]
            count1[c1] = 1 + count1.get(c1, 0)
            if c1 in count1 and count1[c1] == count2[c1]:
                matches += 1
            elif count1[c1] - 1 == count2[c1]:
                matches -= 1
            l += 1
        return matches == 26