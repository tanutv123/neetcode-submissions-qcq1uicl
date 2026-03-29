class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = (bit << (31 - i)) | res
        return res

"""

00000000000000000000000000010101
00000000000000000000000000000010
00000000000000000000000000000000


"""