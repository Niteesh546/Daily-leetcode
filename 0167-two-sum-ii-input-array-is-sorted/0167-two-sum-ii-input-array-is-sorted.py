class Solution(object):
    def twoSum(self, numbers, target):
        left , right = 0, len(numbers)-1
        while left<right:
            c_s = numbers[left]+numbers[right]
            if c_s == target:
                return [left+1,right+1]
            elif c_s < target:
                left +=1
            else:
                right -= 1
        
        