class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        level = 0
        for c in s:
            if c == '(':
                if level > 0:
                    res.append(c)
                level += 1
            else:
                level -= 1
                if level > 0:
                    res.append(c)
        return "".join(res)