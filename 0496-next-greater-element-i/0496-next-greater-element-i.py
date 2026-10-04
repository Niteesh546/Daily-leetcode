class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        next_greater_map = {}
        
        for num in nums2:
            while stack and stack[-1] < num:
                popped_element = stack.pop()
                next_greater_map[popped_element] = num
            stack.append(num)
            
        return [next_greater_map.get(num, -1) for num in nums1]