class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        res = float('-inf')
        while l < r:
            m = l + ((r - l) // 2)
            mid = nums[m]
            if nums[l] > nums[r]:
                if nums[l] <= nums[m]:
                    l = m + 1
                else:
                    r = m
            else:
                r = m
        return nums[l]
