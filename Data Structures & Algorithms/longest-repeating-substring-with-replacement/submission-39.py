class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        maxF = 0
        count = defaultdict(int)
        l = 0
        for r in range(len(s)):
            c = s[r]
            count[c] += 1
            maxF = max(maxF, count[c])
            while r - l + 1 - maxF > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res  