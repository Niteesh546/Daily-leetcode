class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        n9 = sum // 9
        rem = sum% 9
        
        ans = ["9"] * n9
        if rem > 0:
            ans.append(str(rem))
        n0 = num - len(ans)
        ans.extend(["0"] * n0)
        
        return "".join(ans)