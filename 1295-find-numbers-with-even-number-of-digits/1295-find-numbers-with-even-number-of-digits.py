class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count=0
        str_nums = [str(x) for x in nums]
        n=len(nums)
        for i in range(n):

            l=len(str_nums[i])
            if l %2==0:
                count+=1
        return count