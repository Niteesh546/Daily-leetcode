class Solution(object):
    def thirdMax(self, nums):
        n = len(nums)
        nums= sorted(set(nums))

        if len(nums)<3:
            return nums[-1]
        return nums[-3]

        