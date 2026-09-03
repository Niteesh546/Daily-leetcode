class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if min(nums1)%2!=0:
            return True
        else:
            for i in range(len(nums1)):
                if nums1[i]%2==0:
                    continue
                else:
                    return False
        return True

        