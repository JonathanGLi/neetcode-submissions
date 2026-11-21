class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        

        # mono inc to first person taller than themselves
        # n^2, n^2

        #precompute mono increasing

        #10 


        # stack, num eaten, +1 if ends at larger num
        #n, n

        stack =[]
        n = len(heights) #6
        res = n * [0]

        for i in range(n-1, -1, -1):

            count = 0

            while stack and stack[-1] < heights[i]:
                stack.pop()
                count += 1

            if stack:
                count += 1

            stack.append(heights[i])
            res[i] = count

        return res

            

