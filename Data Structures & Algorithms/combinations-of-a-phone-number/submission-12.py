class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letterMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = [""]
        for d in digits:
            tmp = []
            for e in res:
                for c in letterMap[d]:
                    tmp.append(e + c)
            res = tmp
        return res