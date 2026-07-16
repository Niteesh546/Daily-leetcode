class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        m=0
        count=0
        for num in nums:
            if num==1:
                count += 1
            else:
                count = 0
            m = max(m,count)
        return m

        