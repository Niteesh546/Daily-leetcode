class Solution(object):
    def twoSum(self, nums, target):
        has = {}

        for i in range (len(nums)):
            o = target - nums[i]

            if o in has :
                return [has[o],i]
            has[nums[i]]=i      
        

        
        