class Solution:
    def calPoints(self, operations: List[str]) -> int:
        

        stack = []

        for o in operations:
            print(stack)
            if o == '+':
                a = stack[-1]
                b = stack[-2]
                stack.append(a + b)
            elif o == 'C':
                a = stack.pop()
            elif o == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(o))

            
        print(stack)
        res = 0
        for s in stack:
            res += s
        return res