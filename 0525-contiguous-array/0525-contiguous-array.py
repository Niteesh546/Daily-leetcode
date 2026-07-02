class Solution(object):
    def findMaxLength(self, nums):
        map = {0: -1}
        sum = 0
        max_length = 0

        for i in range(len(nums)):
            sum += 1 if nums[i] == 1 else -1
            if sum in map:
                max_length = max(max_length, i - map[sum])
            else:
                map[sum] = i

        return max_length
        