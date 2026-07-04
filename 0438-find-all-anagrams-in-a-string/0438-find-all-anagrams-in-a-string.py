class Solution(object):
    def findAnagrams(self, s, p):
        result = []
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return result

        p_count = [0] * 26
        window_count = [0] * 26
        for i in range(p_len):
            p_count[ord(p[i]) - ord('a')] += 1
            window_count[ord(s[i]) - ord('a')] += 1

        if p_count == window_count:
            result.append(0)

        for i in range(p_len, s_len):
            window_count[ord(s[i]) - ord('a')] += 1           # add new char
            window_count[ord(s[i - p_len]) - ord('a')] -= 1   # remove old char
            if p_count == window_count:
                result.append(i - p_len + 1)

        return result




        