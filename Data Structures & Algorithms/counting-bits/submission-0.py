class Solution:
    def countBits(self, n: int) -> List[int]:
        offset = 1
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp



"""
offset = 4

0 -> 0
1 -> 1 1 + dp[1 - 1] = 1
2 -> 10 1 + dp[2 - 2] = 1
3 -> 11 1 + 1 = 2
4 -> 100
5 -> 101
6 -> 110
7 -> 111
8 -> 1000

"""