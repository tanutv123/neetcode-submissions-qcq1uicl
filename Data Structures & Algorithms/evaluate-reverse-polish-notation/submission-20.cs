public class Solution {
    public int EvalRPN(string[] tokens) {
        var stack = new Stack<int>();
        foreach(var c in tokens) {
            if(c == "+") {
                var int1 = stack.Pop();
                var int2 = stack.Pop();
                stack.Push(int1 + int2);
            } else if(c == "-") {
                var int1 = stack.Pop();
                var int2 = stack.Pop();
                stack.Push(int2 - int1);
            } else if(c == "*") {
                var int1 = stack.Pop();
                var int2 = stack.Pop();
                stack.Push(int1 * int2);
            } else if(c == "/") {
                var int1 = stack.Pop();
                var int2 = stack.Pop();
                stack.Push((int) int2 / int1);
            } else {
                stack.Push(int.Parse(c));
            }
        }
        return stack.Peek();
    }
}
