class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        res = nums[l]
        while l <= r:
            m = l + ((r - l) // 2)
            res = min(nums[m], res)
            if nums[l] > nums[m]:
                r = m - 1
            else:
                if nums[m] < nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return res