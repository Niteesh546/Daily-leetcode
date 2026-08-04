class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        mina=min(nums)
        maxa=max(nums)
        result=[]
        num_set = set(nums)
        for val in range(mina,maxa):
            if val not in num_set:
                result.append(val)
        return result
