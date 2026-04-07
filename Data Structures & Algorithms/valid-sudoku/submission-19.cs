public class Solution {
    public bool IsValidSudoku(char[][] board) {
        var rows = new Dictionary<int, List<char>>();
        var cols = new Dictionary<int, List<char>>();
        var squares = new Dictionary<string, List<char>>();
        for (var r = 0; r < 9; r++) {
            for (var c = 0; c < 9; c++) {
                var n = board[r][c];
                if (n == '.') {
                    continue;
                }
                var invalidRow = rows.ContainsKey(r) && rows[r].Contains(n);
                var invalidCol = cols.ContainsKey(c) && cols[c].Contains(n);
                var squareKey = r / 3 + "," + c / 3;
                var invalidSquare = squares.ContainsKey(squareKey) && squares[squareKey].Contains(n);
                if (invalidRow || invalidCol || invalidSquare) {
                    return false;
                }
                if (!rows.ContainsKey(r)) {
                    rows[r] = new List<char>();
                }
                if (!cols.ContainsKey(c)) {
                    cols[c] = new List<char>();
                }
                if (!squares.ContainsKey(squareKey)) {
                    squares[squareKey] = new List<char>();
                }
                rows[r].Add(n);
                cols[c].Add(n);
                squares[squareKey].Add(n);
            }
        }
        return true;
    }
}
