class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix = [1]*n
        sufix = [1]*n
        out = [0]*n

        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]

        for i in range(n-2,-1,-1):
            sufix[i]=sufix[i+1]*nums[i+1]

        for i in range(n):
            out[i]=prefix[i]*sufix[i]

        return out


        
        