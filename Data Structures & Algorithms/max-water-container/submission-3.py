class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        l = 0
        r = len(heights)-1
        maxx = 0
        while (l < r) :

            w = r - l
            h = min(heights[l], heights[r])

            area = w * h

            maxx = max(maxx, area)

            if (heights[l] > heights[r]):
                r-=1
            else:
                l+=1

        return maxx

