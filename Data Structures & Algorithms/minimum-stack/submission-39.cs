public class MinStack
{
    public Stack<int> stack { get; set; }
    public Stack<int> min { get; set; }
    public MinStack()
    {
        stack = new Stack<int>();
        min = new Stack<int>();
    }

    public void Push(int val)
    {
        stack.Push(val);
        if (min.Count == 0 || val < min.Peek())
        {
            min.Push(val);
        }
        else
        {
            min.Push(min.Peek());
        }
    }

    public void Pop()
    {
        if (stack.Count > 0)
        {
            stack.Pop();
            min.Pop();
        }
    }

    public int Top()
    {
        return stack.Peek();
    }

    public int GetMin()
    {
        return min.Peek();
    }
}
