class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for num in seen:
            if num - 1 not in seen:
                current_num = num
                length = 1
                
                while current_num + 1 in seen:
                    current_num += 1
                    length += 1
                    
                longest = max(length, longest)
                
        return longest                    