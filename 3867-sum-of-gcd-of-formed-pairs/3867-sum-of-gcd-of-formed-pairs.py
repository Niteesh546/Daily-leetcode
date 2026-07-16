import fractions
class Solution(object):
    def gcdSum(self, nums):
        n=len(nums)
        m=0
        prefix=[]
        for x in nums:
            m=max(m,x)
            prefix.append(fractions.gcd(x,m))
        prefix.sort()

        total_sum = 0
        for i in range(n // 2):
            total_sum += fractions.gcd(prefix[i], prefix[n - 1 - i])
            
        return total_sum