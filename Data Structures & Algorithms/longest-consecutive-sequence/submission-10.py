class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)
        nums.sort()

        for i, n in enumerate(nums):
            if n - 1 not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                res = max(res, length)
        return res