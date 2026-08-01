class Solution(object):
    def mySqrt(self, x):
        if x==0:
            return 0
        l=1
        r=x
        ans=1
        while l<=  r:
            mid=(l+r)//2
            mids=mid*mid

            if mids > x:
                r=mid-1
            else:
                ans=mid
                l=l+1
        return ans

        