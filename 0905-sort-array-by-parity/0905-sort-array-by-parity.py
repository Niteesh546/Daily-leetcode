class Solution(object):
    def sortArrayByParity(self, nums):
        n=len(nums)
        front = 0
        back = n-1
        out=[0]*n
        for i in range(n):
            if nums[i]%2==0:
                out[front]=nums[i]
                front += 1
            else:
                out[back]=nums[i]
                back=back-1
        return out
        