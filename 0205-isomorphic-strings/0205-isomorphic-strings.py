class Solution(object):
    def isIsomorphic(self, s, t):
        n=len(s)
        map_st = {}
        map_ts = {}

        for i in range(n):
            if s[i] in map_st and map_st[s[i]] !=t[i]:
                return False
            if t[i] in map_ts and map_ts[t[i]] != s[i]:
                return False
            map_st[s[i]]=t[i]
            map_ts[t[i]]=s[i]
        return True
        
        

        
        