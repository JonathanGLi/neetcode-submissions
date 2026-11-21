class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i = 0
        j = len(heights)-1
        maxContain = 0

        while(i < j):

            shorterHeight = min(heights[i], heights[j])

            contain = (j-i) * shorterHeight
            maxContain = max(maxContain, contain)

            if heights[i] == shorterHeight:
                i+=1
            elif heights[j] == shorterHeight:
                j-=1


        return maxContain
