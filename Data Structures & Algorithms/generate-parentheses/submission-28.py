class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def dfs(open, close):
            if open == close == n:
                res.append("".join(curr))
                return
            
            if open < n:
                curr.append("(")
                dfs(open + 1, close)
                curr.pop()
            if close < open:
                curr.append(")")
                dfs(open, close + 1)
                curr.pop()
        dfs(0, 0)
        return res