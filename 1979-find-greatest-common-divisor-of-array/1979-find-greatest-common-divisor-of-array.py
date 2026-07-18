import math
class Solution(object):
    def findGCD(self, nums):
        min_n = min(nums)
        max_n = max(nums)
        a, b = max_n, min_n
        while b != 0:
            a, b = b, a % b
            
        return a
        