class Solution(object):
    def sumCounts(self, nums):
        total=0
        for i in range(len(nums)):
            seen = set()
            for j in nums[i:]:
                seen.add(j)
                total +=len(seen)*len(seen)
        return total
        