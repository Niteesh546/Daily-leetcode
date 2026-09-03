class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n=len(nums)
        result=[]
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            y=i+1
            z=n-1
            
            while y < z:
                current_sum =nums[i]+nums[y]+nums[z]

                if current_sum < 0:
                    y+=1
                elif current_sum >0:
                    z-=1
                else:
                    result.append([nums[i],nums[y],nums[z]])

                    while y < z and nums[y]==nums[y+1]:
                        y+=1
                    while y<z and nums[z]==nums[z-1]:
                        z-=1
                    y+=1
                    z-=1
        return result


            