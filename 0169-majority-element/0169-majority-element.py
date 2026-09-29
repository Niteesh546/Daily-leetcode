class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums= sorted(nums)
        mid = len(nums)//2
        return nums[mid]