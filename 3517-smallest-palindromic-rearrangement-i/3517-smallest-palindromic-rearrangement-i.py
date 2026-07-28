class Solution(object):
    def smallestPalindrome(self, s):
        n=len(s)
        if n<= 2 :
            return s
        left_half = sorted(s[:n // 2])
        left_str = "".join(left_half)
        right_str=left_str[::-1]

        if n % 2 != 0:
            mid = s[n // 2]
            return left_str + mid + right_str
        else:
            return left_str + right_str



        