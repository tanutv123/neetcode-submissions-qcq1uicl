class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                lc = s[l]
                window[lc] -= 1
                if lc in countT and window[lc] < countT[lc]:
                    have -= 1
                l += 1
            r += 1
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""
                