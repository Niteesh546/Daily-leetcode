class Solution(object):
    def subarraySum(self, nums, k):
        map = {0: 1}
        sum = 0
        count = 0
        for curr in nums:
            sum += curr
            target = sum - k
            if target in map:
                count += map[target]
            map[sum] = map.get(sum, 0) + 1
        return count