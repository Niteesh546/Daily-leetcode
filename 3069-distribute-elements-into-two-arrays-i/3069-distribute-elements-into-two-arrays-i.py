class Solution(object):
    def resultArray(self, nums):
        a1=[nums[0]]
        a2=[nums[1]]

        for x in nums[2:]:
            if a1[-1] > a2[-1]:
                a1.append(x)
            else:
                a2.append(x)
        return a1+a2

        