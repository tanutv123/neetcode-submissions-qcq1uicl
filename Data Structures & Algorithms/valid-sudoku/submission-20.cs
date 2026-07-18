public class Solution {
    public bool IsValidSudoku(char[][] board) {
        var rows = new Dictionary<int, HashSet<int>>();
        var cols = new Dictionary<int, HashSet<int>>();
        var squares = new Dictionary<string, HashSet<int>>();

        for (int r = 0; r < board.Length; r++) {
            for (int c = 0; c < board.Length; c++) {
                if (board[r][c] == '.') {
                    continue;
                }
                int n = board[r][c];
                var invalidRow = rows.ContainsKey(r) && rows[r].Contains(n);
                var invalidCol = cols.ContainsKey(c) && cols[c].Contains(n);
                var squareKey = (r / 3) + "," + (c / 3);
                var invalidSquare = squares.ContainsKey(squareKey) && squares[squareKey].Contains(n);
                if (invalidRow || invalidCol || invalidSquare) {
                    Console.WriteLine(r);
                    Console.WriteLine(c);
                    Console.WriteLine(squareKey);
                    return false;
                } 
                if (!rows.ContainsKey(r)) {
                    rows.Add(r, new HashSet<int>());
                } 
                if (!cols.ContainsKey(c)) {
                     cols.Add(c, new HashSet<int>());
                } 
                if (!squares.ContainsKey(squareKey)) {
                     squares.Add(squareKey, new HashSet<int>());
                } 
                rows[r].Add(n);
                cols[c].Add(n);
                squares[squareKey].Add(n);
            }
        }
        return true;
    }
}
