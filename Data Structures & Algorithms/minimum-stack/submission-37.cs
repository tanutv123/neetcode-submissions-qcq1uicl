public class MinStack {
    Stack<int> stack = new Stack<int>();
    Stack<int> minStack = new Stack<int>();
    public MinStack() {
        
    }
    
    public void Push(int val) {
        stack.Push(val);
        val = Math.Min(val, minStack.Count == 0 ? val : minStack.Peek());
        minStack.Push(val);
    }
    
    public void Pop() {
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
