class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l_max=float('-inf')
        r_max=float('-inf')
        left_max=[0]*n
        right_max=[0]*n

        for i in range(n):
            l_max=max(height[i],l_max)
            left_max[i]=l_max
        print(left_max)

        for i in range(n-1,-1,-1):
            r_max=max(height[i],r_max)
            right_max[i]=r_max
        print(left_max)
        
        #[0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
        #[3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
        total_area=0
        for i in range(n):
            area=min(right_max[i],left_max[i])-height[i]
            if area > 0 :
                total_area += area
        print(total_area)
        return total_area