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
        q = deque()
        q.append([])
        res = []
        for i in range(len(digits)):
            for _ in range(len(q)):
                arr = q.popleft()
                for c in digitMap[digits[i]]:
                    copy = arr.copy()
                    copy.append(c)
                    q.append(copy)

        return ["".join(element) for element in q]