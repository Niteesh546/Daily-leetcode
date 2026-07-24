class Solution(object):
    def searchRange(self, nums, target):
        result=[]
        if target not in nums:
            return [-1,-1]
        
        for i in range(len(nums)):
            if nums[i]==target:
                result.append(i)
        if len(result)==1:
            result.append(result[0])
        if len(result)>2:
            return [result[0],result[len(result)-1]]
        return result


        
        