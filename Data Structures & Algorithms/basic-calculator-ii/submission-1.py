class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        num = 0
        op = '+'
        s = s.replace(' ', '')
        n = len(s)



        for i, c in enumerate(s):
            print(c)
            print(stack)
            print(op)
            print('i', i)
            print(n-1)

            if c.isdigit():
                num = num*10 + int(c)
            if (not c.isdigit()) or i == n-1:
                print("hi1")
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    a = stack.pop()
                    stack.append(num * a)
                elif op == '/':
                    print("hi")
                    a = stack.pop()
                    stack.append(int(a / num))

                op = c
                num = 0

        return sum(stack)


        # 3+
        #stack(3, 4)
        #num = 2
        #op = +




