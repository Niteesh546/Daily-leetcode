class Solution(object):
    def findDuplicate(self, nums):
        hash_map={}
        for num in nums:
            if num in hash_map:
                return num
            hash_map[num]=num
        