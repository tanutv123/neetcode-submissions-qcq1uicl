class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(n, curr):
            if n == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[n])
            dfs(n + 1, curr)
            curr.pop()

            dfs(n + 1, curr)
        
        dfs(0, [])
        return res