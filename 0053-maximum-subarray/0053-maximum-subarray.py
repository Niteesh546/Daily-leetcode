class Solution(object):
    def maxSubArray(self, nums):
        curr_sum = 0
        maxi_s = nums[0]
        for num in nums:
            curr_sum = curr_sum+num

            if curr_sum > maxi_s:
                maxi_s = curr_sum
            if curr_sum < 0:
                curr_sum=0
        return maxi_s
        