public class Solution {
    public bool IsValidSudoku(char[][] board) {
        var rows = new Dictionary<int, HashSet<char>>();
        var cols = new Dictionary<int, HashSet<char>>();
        var square = new Dictionary<string, HashSet<char>>();
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                var ch = board[r][c];
                if (ch == '.') {
                    continue;
                }
                var squareKey = $"{r / 3}, {c / 3}";
                if ((rows.ContainsKey(r) && rows[r].Contains(ch)) || (cols.ContainsKey(c) && cols[c].Contains(ch)) || (square.ContainsKey(squareKey) && square[squareKey].Contains(ch))) {
                    return false;
                }
                if (!rows.ContainsKey(r)) {
                    rows.Add(r, new HashSet<char>());
                }
                if (!cols.ContainsKey(c)) {
                    cols.Add(c, new HashSet<char>());
                }
                if (!square.ContainsKey(squareKey)) {
                    square.Add(squareKey, new HashSet<char>());
                }
                rows[r].Add(ch);
                cols[c].Add(ch);
                square[squareKey].Add(ch);
            }
        }
        return true;
    }
}
