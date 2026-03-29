public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        var COLS = matrix[0].Length;
        var ROWS = matrix.Length;

        var top = 0;
        var bot = ROWS -1;
        while(top <= bot) {
            int mid = (top + bot) / 2;
            if(target > matrix[mid][COLS - 1]) {
                top = mid + 1;
            } else if(target < matrix[mid][0]) {
                bot = mid - 1;
            } else {
                break;
            }
        }

        int row = (top + bot) / 2;
        int l = 0;
        int r = COLS - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if(target < matrix[row][mid]) {
                r = mid - 1;
            } else if(target > matrix[row][mid]) {
                l = mid + 1;
            } else {
                return true;
            }
        }
        return false;
    }
}
