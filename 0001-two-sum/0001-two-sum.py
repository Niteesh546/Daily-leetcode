class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for i in range(len(nums)):
            des = target-nums[i]
            if des in hash_map:
                return [hash_map[des],i]
            hash_map[nums[i]]=i

        

        
        