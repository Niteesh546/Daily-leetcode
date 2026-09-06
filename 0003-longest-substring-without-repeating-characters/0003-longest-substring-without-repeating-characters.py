class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        se=set()
        l=0
        long=0
        for i in range(n):
            while s[i] in se:
                se.remove(s[l])
                l=l+1
            w = (i- l)+1
            long = max(long,w)
            se.add(s[i])
        return long

                    