class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zero_count = 1, 0

        for n in nums:
            if n:
                product *= n
            else:
                zero_count += 1
        if zero_count > 1: return [0] * len(nums)

        res = [0] * len(nums)

        for i, n in enumerate(nums): 
            if zero_count: res[i] = 0 if n else product
            else: res[i] = product // n
        return res
        