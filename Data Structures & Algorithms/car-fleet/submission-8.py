class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort()

        stack = []

        for i in range(len(position)):
            time_needed = (target - pair[i][0]) / pair[i][1]

            while (stack and stack[-1] <= time_needed):
                stack.pop()

            stack.append(time_needed)

        return len(stack)

        # 6 9 10 3
        # 3 4.5 10 3

        # 3 6 9 10
        # 3 3 4.5 10

        # 10 3