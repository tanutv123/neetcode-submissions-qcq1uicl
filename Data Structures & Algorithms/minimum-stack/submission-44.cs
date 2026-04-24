public class MinStack {
    private Stack<int> stack;
    private Stack<int> minStack;
    public MinStack() {
        stack = new();
        minStack = new();
    }
    
    public void Push(int val) {
        stack.Push(val);
        var min = Math.Min(minStack.Any() ? minStack.Peek() : val, val);
        minStack.Push(min);
    }
    
    public void Pop() {
        if (stack.Count == 0) return;
        stack.Pop();
        minStack.Pop();
    }
    
    public int Top() {
        return stack.Peek();
    }
    
    public int GetMin() {
        return minStack.Peek();
    }
}
