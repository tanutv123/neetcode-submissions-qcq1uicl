class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')
        while l <= r:
            m = l + ((r - l) // 2)
            res = min(nums[m], res)
            if nums[r] > nums[m]:
                r = m - 1
            else:
                l = m + 1
        return res