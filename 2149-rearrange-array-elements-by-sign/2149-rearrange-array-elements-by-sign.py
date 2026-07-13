class Solution(object):
    def rearrangeArray(self, nums):
        n=len(nums)
        out=[0]*n
        pos = 0
        neg = 1
        for i in range(n):
            if nums[i]>0:
                out[pos]=nums[i]
                pos +=2
            else:
                out[neg]=nums[i]
                neg +=2
        return out
        