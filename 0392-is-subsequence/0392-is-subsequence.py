class Solution(object):
    def isSubsequence(self, s, t):
        i=0
        for j in range(len(t)):
            if i ==len(s):
                return True
            if s[i]==t[j]:
                i=i+1
        return len(s)==i

        