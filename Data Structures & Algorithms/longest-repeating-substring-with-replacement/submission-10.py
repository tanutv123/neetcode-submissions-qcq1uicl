class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = 0
        res = 0
        l = 0   
        count = {}

        for r in range(len(s)):
            rc = s[r]
            count[rc] = count.get(rc, 0) + 1
            maxF = max(maxF, count[rc])

            if r - l - maxF >= k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
