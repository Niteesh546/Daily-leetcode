class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        total_score = 0
        depth = 0
        for i, char in enumerate(s):
            if char == '(':
                depth += 1
            else:
                depth -= 1
                if s[i - 1] == '(':
                    total_score += 1 << depth
        return total_score