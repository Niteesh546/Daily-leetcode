class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [-1] * n
        
        for i in range(n):
            for j in range(1, n):
                next_idx = (i + j) % n
                if nums[next_idx] > nums[i]:
                    res[i] = nums[next_idx]
                    break
                    
        return res
