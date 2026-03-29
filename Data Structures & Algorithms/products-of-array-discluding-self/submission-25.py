class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        res = [0] * len(nums)

        for n in nums:
            if not n:
                zero_count += 1
            else:
                product *= n
        if zero_count > 1:
            return [0] * len(nums)
        
        for i, n in enumerate(nums):
            if zero_count > 0:
                res[i] = 0 if n else product
            else:
                res[i] = product // n
        return res