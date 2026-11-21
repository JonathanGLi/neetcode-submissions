class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        # max recatngle has an index with min height which is the hieght of the rectangle

        stack = []

        left = [-1] * len(heights) # left bound of height[i]

        for i in range(len(heights)):
            while (stack and heights[stack[-1]] >= heights[i]):
                stack.pop()
            if stack:
                left[i] = stack[-1]

            stack.append(i)

        print(left)

        stack = []
        right = [len(heights)] * len(heights)

        for i in range(len(heights)-1, -1, -1):
            while (stack and heights[stack[-1]] >= heights[i]):
                stack.pop()
            if stack:
                right[i] = stack[-1]

            stack.append(i)

        print(right)

        maxx = 0
        for i in range(len(heights)):
            rect = heights[i] * (right[i] - left[i]-1)
            maxx = max(maxx, rect)
            print(rect)

        return maxx