class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        prefix_max=[0]*len(nums)
        sufix_min=[0]*len(nums)
        maxi=float('-inf')
        mini=float('inf')

        for i in range(n):
            maxi=max(maxi,nums[i])
            prefix_max[i]=maxi
            print(prefix_max)

        for i in range(n-1,-1,-1):
            mini=min(mini,nums[i])
            sufix_min[i]=mini
            print(sufix_min)

        for i in range(n):
            result=prefix_max[i]-sufix_min[i]
            if result<=k:
                print(i)
                return i
        return -1