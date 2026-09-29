class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                if nums[i] in hashmap:
                    hashmap[nums[i]] += 1  
                else:
                    hashmap[nums[i]] = 1   
        print(hashmap)
        if len(hashmap)==0:
            return -1
        max_freq = -1
        result = -1
        for num, freq in hashmap.items():
            if freq > max_freq:
                max_freq = freq
                result = num
            elif freq == max_freq:
                result = min(result, num)
                
        return result
