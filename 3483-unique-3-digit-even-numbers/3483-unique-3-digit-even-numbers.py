class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        available_counts = [0] * 10
        for d in digits:
            available_counts[d] += 1
            
        distinct_even_count = 0
        
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            needed_counts = [0] * 10
            needed_counts[d1] += 1
            needed_counts[d2] += 1
            needed_counts[d3] += 1
            
            if (available_counts[d1] >= needed_counts[d1] and 
                available_counts[d2] >= needed_counts[d2] and 
                available_counts[d3] >= needed_counts[d3]):
                distinct_even_count += 1
                
        return distinct_even_count