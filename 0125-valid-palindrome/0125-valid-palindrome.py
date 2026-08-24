class Solution(object):
    def isPalindrome(self, s):
        new_string = ""
        for char in s:
            if char.isalnum():
                new_string +=char.upper()
        return new_string==new_string[::-1]
        