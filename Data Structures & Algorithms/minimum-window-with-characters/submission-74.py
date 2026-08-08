class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have, need = 0, len(set(t))
        count1 = defaultdict(int)
        for c in t:
            count1[c] += 1
        
        count2 = defaultdict(int)
        l = 0
        res = []
        for r in range(len(s)):
            c = s[r]
            count2[c] += 1
            if count2[c] == count1[c]:
                have += 1
            while l <= r and have == need:
                if not res or (res[1] - res[0] + 1) > (r - l + 1):
                    res = [l, r]
                c = s[l]
                count2[c] -= 1
                l += 1
                if count2[c] == count1[c] - 1:
                    have -= 1
        return s[res[0]:(res[1] + 1)] if res else ""
