class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        res = float('inf')
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[l] > nums[r]:
                if nums[l] <= nums[m]:
                    l = m + 1
                else:
                    r = m - 1
                res = min(res, nums[m])
            else:
                res = min(res, nums[l])
                break
        return res