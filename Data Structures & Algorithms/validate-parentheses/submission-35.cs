public class Solution {
    public bool IsValid(string s) {
        var dict = new Dictionary<char, char>
        {
            { ')', '(' },
            { ']', '[' },
            { '}', '{' },
        };
        var stack = new Stack<char>();

        for (int i = 0; i < s.Length; i++)
        {
            if (!dict.ContainsKey(s[i]))
            {
                stack.Push(s[i]);
                continue;
            } 
            else
            {
                if (stack.Count <= 0 || stack.Peek() != dict[s[i]]) {
                    return false;
                }
                stack.Pop();
            }
        }
        return stack.Count == 0;
    }
}

/*
([{}))


*/