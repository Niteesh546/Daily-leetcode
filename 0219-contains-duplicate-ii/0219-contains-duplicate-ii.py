class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        for i, val in enumerate(nums):
            if val in seen:
                if i-seen[val]<=k:
                    return True
            seen[val]=i
        return False