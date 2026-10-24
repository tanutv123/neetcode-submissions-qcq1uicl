class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        visit = [False] * len(digits)
        word = []
        def backtrack(i):
            if i == len(digits):
                res.append("".join(word.copy()))
                return
            for c in digitMap[digits[i]]:
                word.append(c)
                backtrack(i + 1)
                word.pop()
        backtrack(0)
        return res