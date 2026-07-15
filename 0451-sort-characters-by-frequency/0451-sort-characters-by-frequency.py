class Solution(object):
    def frequencySort(self, s):
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        sorted_chars = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
        res = []
        for char in sorted_chars:
            res.append(char * counts[char])
            
        return "".join(res)
        