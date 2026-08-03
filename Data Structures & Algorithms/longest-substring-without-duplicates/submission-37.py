class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        l, r = 0, 1
        store = set(s[0])
        res = 0
        while (r < n):
            c = s[r]
            if c in store:
                while c in store and l <= r:
                    store.remove(s[l])
                    l += 1
            res = max(res, r - l + 1)
            store.add(c)
            r += 1
        return res
            
