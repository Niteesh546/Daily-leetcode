class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums11 = nums1[:m]
        nums22 = nums2[:n]
        nums1[:] = sorted(nums11+nums22)
        
        return nums1

        