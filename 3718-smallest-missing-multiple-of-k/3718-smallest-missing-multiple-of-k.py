class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        j=0
        for i in range(len(nums)):
            j=j+1
            total = j*k
            if total not in nums:

                return total
        return max(nums)+k
