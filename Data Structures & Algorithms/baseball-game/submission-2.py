class Solution:
    def calPoints(self, operations: List[str]) -> int:
        

        stack = []


        for o in operations:

            print(o)

            if o == '+':
                a = stack[-2]
                b = stack[-1]
                stack.append(a+b)
            elif o == 'D':
                a = stack[-1]
                stack.append(a*2)
            elif o == 'C':
                stack.pop()
            else:
                stack.append(int(o))
            
            print(stack)


        return sum(stack)