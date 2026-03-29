public class Solution {
    public int EvalRPN(string[] tokens) {
        var stack = new Stack<int>();
        foreach(var c in tokens) {
            if(c == "+") {
                stack.Push(stack.Pop() + stack.Pop());
            } else if(c == "-") {
                int v1 = stack.Pop();
                int v2 = stack.Pop();
                stack.Push(v2 - v1);
            } else if(c == "*") {
                stack.Push(stack.Pop() * stack.Pop());
            } else if(c == "/") {
                int v3 = stack.Pop();
                int v4 = stack.Pop();
                stack.Push((int)((double)v4 / v3));
            } else {
                stack.Push(int.Parse(c));
            }
        }
        return stack.Peek();
    }
}
