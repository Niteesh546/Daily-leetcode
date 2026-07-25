class Solution(object):
    def maxProduct(self, n):
        arr=[]
        while n > 0:
            d=n%10
            arr.append(d)
            n = n//10
        arr.sort()
        return arr[-1]*arr[-2]


        