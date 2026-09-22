class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_sum = 0
        for x in nums:
            if x < 10:
                single_sum += x
        total_sum = sum(nums) 
        double_sum = total_sum - single_sum
        return single_sum != double_sum