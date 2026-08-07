class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        pushes = 0
        pushes += min(n, 8) * 1
        if n <= 8:
            return pushes

        pushes += min(n - 8, 8) * 2
        if n <= 16:
            return pushes
    
        pushes += min(n - 16, 8) * 3
        if n <= 24:
            return pushes
        
        pushes += (n - 24) * 4
        return pushes
    