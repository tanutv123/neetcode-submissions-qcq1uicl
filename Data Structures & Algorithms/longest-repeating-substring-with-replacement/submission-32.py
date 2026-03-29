class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = 0
        fMap = {}
        l = 0
        res = 0
        for r in range(len(s)):
            c = s[r]
            fMap[c] = fMap.get(c, 0) + 1
            maxF = max(fMap[c], maxF)
            if r - l - maxF >= k:
                fMap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res
