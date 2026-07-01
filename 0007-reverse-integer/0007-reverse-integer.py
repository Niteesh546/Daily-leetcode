class Solution(object):
    def reverse(self, x):
        if x<0:
            sign =-1
        else:
            sign=1
        x=abs(x)
        revers = 0
        while x > 0:
            i = x % 10
            revers = (revers * 10) + i
            x =x//10
        revers *= sign
        if revers < -2**31 or revers > 2**31-1:
            return 0
        return revers
    

        
        