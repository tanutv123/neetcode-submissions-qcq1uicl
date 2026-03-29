public class Solution {
    public int MinEatingSpeed(int[] piles, int h) {
        int l = 1;
        int r = piles.Max();
        int res = 0;

        while (l <= r) {
            int m = (l + r) / 2;
            int totalTime = 0;
            foreach(var p in piles) {
                totalTime += (int)Math.Ceiling((double)p / m);
            }

            if (totalTime <= h) {
                res = m;
                r = m - 1;
            } else{
                l = m + 1;
            }
        }
        return res;
    }
}
