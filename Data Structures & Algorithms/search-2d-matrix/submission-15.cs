public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        int ROWS = matrix.Length;
        int COLS = matrix[0].Length;

        int top = 0;
        int bot = ROWS - 1;
        while(top <= bot) {
            int mid = top + (bot - top) / 2;
            if(matrix[mid][0] > target) {
                bot = mid - 1;
            } else if(matrix[mid][COLS - 1] < target) {
                top = mid + 1;
            } else {
                break;
            }
        }
        if(!(top <= bot)) {
            return false;
        }

        int row = top + (bot - top) / 2;
        int l = 0;
        int r = COLS - 1;
        while(l <= r) {
            int mid = l + (r - l) / 2;
            if(matrix[row][mid] < target) {
                l = mid + 1;
            } else if(matrix[row][mid] > target) {
                r = mid - 1;
            } else {
                return true;
            }
        }
        return false;
    }
}
