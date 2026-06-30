class Solution(object):
    def numberOfSubstrings(self, s):
        last_seen ={'a': -1, 'b': -1, 'c': -1}
        count = 0
        for right, char in enumerate(s):
            last_seen[char] = right
            if min(last_seen.values()) != -1:
                count += min(last_seen.values()) + 1
        return count
            
        