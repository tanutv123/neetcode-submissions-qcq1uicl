class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            rc = s[r]
            window[rc] = window.get(rc, 0) + 1
            if rc in countT and window[rc] == countT[rc]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                lc = s[l]
                window[lc] -= 1
                if lc in countT and countT[lc] > window[lc]:
                    have -= 1            
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""
        