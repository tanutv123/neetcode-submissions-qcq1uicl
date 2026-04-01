public class Solution {
    public bool IsValidSudoku(char[][] board) {
        var rows = new Dictionary<int, HashSet<char>>();
        var cols = new Dictionary<int, HashSet<char>>();
        var square = new Dictionary<string, HashSet<char>>();
        for (int row = 0; row < 9; row++)
        {
            for (int col = 0; col < 9; col++)
            {
                if (board[row][col] == '.') continue;
                var squareKey = $"{row / 3}, {col / 3}";
                if ((rows.ContainsKey(row) && rows[row].Contains(board[row][col])) || (cols.ContainsKey(col) && cols[col].Contains(board[row][col])) || (square.ContainsKey(squareKey) && square[squareKey].Contains(board[row][col])))
                {
                    return false;
                }

                if (!rows.ContainsKey(row)) rows[row] = new HashSet<char>();
                if (!cols.ContainsKey(col)) cols[col] = new HashSet<char>();
                if (!square.ContainsKey(squareKey)) square[squareKey] = new HashSet<char>();

                rows[row].Add(board[row][col]);
                cols[col].Add(board[row][col]);
                square[squareKey].Add(board[row][col]);
            }
        }
        
        return true;
    }
}
