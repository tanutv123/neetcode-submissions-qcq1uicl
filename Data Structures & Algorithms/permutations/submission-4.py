class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0, nums)
    
    def helper(self, i, nums):
        if i == len(nums):
            return [[]]  # Base case: Return an empty list inside a list
        
        res = []
        perms = self.helper(i + 1, nums)  # Get permutations of the rest of the list
        for p in perms:  # Don't modify perms while iterating
            for j in range(len(p) + 1):
                copy = p.copy()
                copy.insert(j, nums[i])  # Insert nums[i] at different positions
                res.append(copy)  # Store the new permutation in res
        
        return res  # Return the new list of permutations
