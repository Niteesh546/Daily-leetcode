class Solution(object):
    def isPalindrome(self, x):
        reverse=0
        ox=x
        while x> 0:
            i = x%10
            reverse = (reverse*10) + i
            x=x//10
        return ox==reverse
        
        