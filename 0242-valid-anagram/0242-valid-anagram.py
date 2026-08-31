class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counts={}
        countt={}
        for i in range(len(s)):
            chars,chart=s[i],t[i]


            if chars in counts:
                counts[s[i]]+=1
            else:
                counts[s[i]] =1
            
            if chart in countt:
                countt[t[i]]+=1
            else:
                countt[t[i]] =1
        return counts==countt