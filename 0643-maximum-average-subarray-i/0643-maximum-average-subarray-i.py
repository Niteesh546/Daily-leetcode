class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sliding_sum = sum(nums[:k])
        maximum_sum = sliding_sum
        n=len(nums)
        for i in range(k,n):
            sliding_sum += nums[i]-nums[i-k]
            maximum_sum = max(sliding_sum,maximum_sum)
        return maximum_sum/k