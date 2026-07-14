class Solution(object):
    def maxFrequencyElements(self, nums):
        seen = {}

        for num in nums:
            if num in seen:
                seen[num] +=1
            else:
                seen[num] = 1
        maxi = max(seen.values())
        result =0
        for key, val in seen.items():
            if val == maxi:
                result +=val
        return result

            

        