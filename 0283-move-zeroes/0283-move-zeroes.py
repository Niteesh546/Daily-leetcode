class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        r=0
        l=0
        n=len(nums)
        while r<n:
            if nums[r]!=0:
                nums[r],nums[l]=nums[l],nums[r]
                l=l+1
            r=r+1
        return nums
        
        