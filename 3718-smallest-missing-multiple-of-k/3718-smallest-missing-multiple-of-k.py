class Solution(object):
    def missingMultiple(self, nums, k):
        i=1
        while True:
            target = i*k
            i=i+1
            if target in nums:
                continue
            else:
                return target

        