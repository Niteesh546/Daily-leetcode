class Solution(object):
    def climbStairs(self, n):
        if n < 3 :
            return n
        f=1
        s=2
        c=0
        for i in range(2,n):
            c =f+s
            f =s 
            s=c
        return c

        
        