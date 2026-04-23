public class MinStack {
    private long min;
    private Stack<long> stack;
    public MinStack() {
        stack = new();
    }
    
    public void Push(int val) {
        if (stack.Count == 0) {
            stack.Push(0L);
            min = (long)val;
        }
        else {
            stack.Push((long)val - min);
            if (val < min) min = (long)val;
        }
    }
    
    public void Pop() {
        if (stack.Count == 0) return;
        var pop = stack.Pop();
        if (pop < 0) min -= pop;        
    }
    
    public int Top() {
        var top = stack.Peek();
        return top < 0 ? (int)min : (int)(top + min);
    }
    
    public int GetMin() {
        return (int)min;
    }
}
