class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set = set(nums) 

        for j in range(1, len(nums) + 2):
            total = j * k
            if total not in num_set:
                return total
