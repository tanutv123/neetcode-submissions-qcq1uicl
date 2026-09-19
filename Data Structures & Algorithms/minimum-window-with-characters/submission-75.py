class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count1, count2 = defaultdict(int), defaultdict(int)
        for c in t:
            count1[c] += 1
        
        have, need = 0, len(count1)
        res = []
        resLen = float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            count2[c] += 1
            if count2[c] == count1[c]:
                have += 1
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                c = s[l]
                count2[c] -= 1
                if count2[c] == count1[c] - 1:
                    have -= 1
                l += 1
        return "" if resLen == float("inf") else s[res[0]:res[1] + 1]
            


