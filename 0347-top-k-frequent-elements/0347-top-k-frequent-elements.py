class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        

        arr=[]
        for num,con in hashmap.items():
            arr.append([con,num])
        arr.sort()
        
        
        result=[]
        while len(result)<k:
            pop_i = arr.pop()
            number = pop_i[1]
            result.append(number)
        return result

            