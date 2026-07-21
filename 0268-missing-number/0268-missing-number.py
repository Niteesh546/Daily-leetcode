class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        s=sorted(nums)
        for i in range(n):
            if i != s[i]:
                return i
        return n

        