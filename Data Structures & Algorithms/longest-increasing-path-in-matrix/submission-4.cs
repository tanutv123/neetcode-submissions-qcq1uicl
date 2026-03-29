public class Solution
{
    private int[][] directions = new int[][]
    {
        new int[] { 1, 0 },
        new int[] { -1, 0 },
        new int[] { 0, 1 },
        new int[] { 0, -1 }
    };
    public int LongestIncreasingPath(int[][] matrix)
    {
        int ROWS = matrix.Length, COLS = matrix[0].Length;
        int res = 0;
        for (int r = 0; r < ROWS; r++)
        {
            for (int c = 0; c < COLS; c++)
            {
                res = Math.Max(res, dfs(r, c, int.MinValue, matrix));
            }
        }
        return res;
    }

    public int dfs(int r, int c, int prevVal, int[][] matrix)
    {
        if (Math.Min(r, c) < 0
        || r >= matrix.Length
        || c >= matrix[0].Length
        || matrix[r][c] <= prevVal)
        {
            return 0;
        }

        int res = 1;
        foreach (var dir in directions)
        {
            res = Math.Max(res, 1 + dfs(r + dir[0],
                                    c + dir[1], matrix[r][c], matrix));
        }

        return res;
    }
}
