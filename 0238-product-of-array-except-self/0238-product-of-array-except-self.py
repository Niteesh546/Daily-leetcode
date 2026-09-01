class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix_sum = [1]*n
        print(prefix_sum)
        sufix_sum = [1]*n
        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1]*nums[i-1]
        print(prefix_sum)

        for i in range(n-2,-1,-1):
            sufix_sum[i] = sufix_sum[i+1]*nums[i+1]
        print(sufix_sum)
        res=[1]*n
        for i in range(n):
            res[i]=prefix_sum[i]*sufix_sum[i]
        print(res)
        return res