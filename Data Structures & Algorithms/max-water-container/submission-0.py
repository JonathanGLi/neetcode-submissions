class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        m = 0
        l, r = 0, len(heights)-1

        while l < r:

            waterHeight = min(heights[l], heights[r])
            m = max(m, waterHeight*(r-l))

            if heights[l] == waterHeight:
                l+=1
            else:
                r-=1

        return m