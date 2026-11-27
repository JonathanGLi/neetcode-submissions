class Solution:
    def trap(self, height: List[int]) -> int:
        

        l = 0
        r = len(height)-1

        left_max_height = height[l]
        right_max_height = height[r]

        total_water = 0

        while l < r:

            if height[l] > height[r]:
                total_water += (right_max_height - height[r])
                r-=1
                right_max_height = max(right_max_height, height[r])

            if height[l] <= height[r]:
                total_water += (left_max_height - height[l])
                l+=1
                left_max_height = max(left_max_height, height[l])

        return total_water


