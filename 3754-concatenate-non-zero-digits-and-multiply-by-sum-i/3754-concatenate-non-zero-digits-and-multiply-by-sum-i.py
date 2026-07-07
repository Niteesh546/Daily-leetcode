class Solution(object):
    def sumAndMultiply(self, n):
        x = list(str(n))
        while "0" in x:
            x.remove("0")
        if not x:
            return 0
        xc = "".join(x)
        s =0
        for num in x:
            s = s + int(num)

        return s * int(xc)

        