class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = float('-inf')
        res = [0, 0]
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if self.isPalindrome(s[i:j+1]) and resLen < j - i + 1:
                    resLen = j - i + 1
                    res[0] = i
                    res[1] = j
        return s[res[0]:res[1]+1]
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        