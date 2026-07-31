class Solution(object):
    def peakIndexInMountainArray(self, arr):
        max_a=max(arr)
        idx=arr.index(max_a)
        return idx
        