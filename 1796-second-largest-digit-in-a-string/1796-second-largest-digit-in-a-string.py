class Solution(object):
    def secondHighest(self, s):
        digits = set()

        for char in s:
            if char.isdigit():
                char = int(char)
                digits.add(char)
        sorted_digits=sorted(list(digits))

        if len(sorted_digits)<2:
            return -1
        return sorted_digits[-2]
        