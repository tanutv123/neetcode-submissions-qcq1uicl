class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        nums = self.nums
        flag = False
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= val:
                nums.insert(i + 1, val)
                flag = True
                break
        if not flag:
            nums.insert(0, val)
        return nums[len(nums) - self.k]
            
