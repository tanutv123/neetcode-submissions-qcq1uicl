class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def valid(s: str):
            openN = 0
            for c in s:
                openN += 1 if c == '(' else -1
                if openN < 0:
                    return False
            return not openN
        def dfs(s: str):
            if n * 2 == len(s):
                if valid(s):
                    res.append(s)
                return
            dfs(s + '(')
            dfs(s + ')')
        dfs("")
        return res