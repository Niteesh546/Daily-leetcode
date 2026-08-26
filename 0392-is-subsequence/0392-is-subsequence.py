class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        for j in range(len(t)):
            if len(s)==i:
                return True
            if s[i]==t[j]:
                i=i+1
            
        print(i)
        print(len(s))
        return len(s)==i
