public class Solution {
    public int EvalRPN(string[] tokens) {
        var res = 0;
        var stack = new Stack<int>();
        for (int i = 0; i < tokens.Length; i++) {
            var c = tokens[i];
            if (c == "+") {
                stack.Push(stack.Pop() + stack.Pop());
            }
            else if (c == "-") {
                var a = stack.Pop();
                var b = stack.Pop();
                stack.Push(b - a);
            }
            else if (c == "*") {
                stack.Push(stack.Pop() * stack.Pop());
            }
            else if (c == "/") {
                var a = stack.Pop();
                var b = stack.Pop();
                stack.Push((int)Math.Truncate((double)b / a));
            }
            else {
                stack.Push(int.Parse(c));
            }
        }
        return stack.Peek();
    }
}
