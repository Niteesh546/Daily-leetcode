class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
         hashmap ={}
         for i in range(len(numbers)):
            find = target-numbers[i]
            if find in hashmap:
                return [hashmap[find]+1,i+1]
            hashmap[numbers[i]] = i
        