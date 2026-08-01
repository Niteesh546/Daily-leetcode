class Solution(object):
    def shiftGrid(self, grid, k):
        rows=len(grid)
        cols=len(grid[0])
        n=rows*cols
        if n==1:
            return grid
        k = k % n

        def reverse(i,j):
            while i<=j:
                grid[i//cols][i%cols],grid[j//cols][j%cols]=grid[j//cols][j%cols],grid[i//cols][i%cols]
                i=i+1
                j=j-1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)

        return grid