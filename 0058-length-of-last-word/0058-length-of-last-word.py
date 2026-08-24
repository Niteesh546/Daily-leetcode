class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words =s.split()
        x = "".join(words[-1])
        return len(x)
        