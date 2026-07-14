class Solution(object):
    def sortArrayByParityII(self, nums):
        n = len(nums)
        out = [0]*n
        even=0
        odd=1
        for i in range(n):
            if nums[i]%2==0:
                out[even]=nums[i]
                even += 2
            else:
                out[odd]=nums[i]
                odd += 2
        return out
        