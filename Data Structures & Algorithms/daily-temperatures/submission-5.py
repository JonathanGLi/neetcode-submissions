class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0 for i in range(len(temperatures))]

        for i, t in enumerate(temperatures):

            while (stack and stack[-1][0] < t):
                [t_t, t_i] = stack.pop()
                res[t_i] = i - t_i
            stack.append([t, i])
        return res
                

