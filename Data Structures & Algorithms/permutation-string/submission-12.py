class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = {}

        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        for i in range(len(s2)):
            count2, curr = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)

                if count1.get(s2[j], 0) < count2.get(s2[j], 0):
                    break
                if count2.get(s2[j], 0) == count1.get(s2[j]):
                    curr += 1
                if curr == len(count1):
                    return True
        return False