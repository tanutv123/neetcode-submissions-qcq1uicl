class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res.append("")
        for d in digits:
            tmp = []
            for s in res:
                for c in digitToChar[d]:
                    tmp.append(s + c)
            res = tmp
        return res
