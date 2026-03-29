public class Solution {  
    public List<string> GenerateParenthesis(int n) {
        List<string> res = new List<string>();
        Stack<string> stack = new Stack<string>();
        Dfs(n, 0, 0, stack, res);
        return res;
    }

    public void Dfs(int n, int openN, int closeN, Stack<string> stack, List<string> res) {
        if(n == openN && n == closeN) {
            res.Add(string.Join("", stack));
            return;
        }

        if(openN < n) {
            stack.Push(")");
            Dfs(n, openN + 1, closeN, stack, res);
            stack.Pop();
        }

        if(closeN < openN) {
            stack.Push("(");
            Dfs(n, openN, closeN + 1, stack, res);
            stack.Pop();
        }
    }
}
