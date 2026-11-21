class Solution:
    def decodeString(self, s: str) -> str:
        


        # stack
        stack = []

        cur = ""
        num = 0

        for c in s:
            print(c)
            print(stack)
            #if number, push onto stack
            if c.isdigit():
                num = 10 * num + int(c)
            # if[ [reset cur
            elif c == '[':
                if len(cur) > 0:
                    stack.append(cur)
                stack.append(num)
                num = 0
                cur = ""
            # when fin d], pop until find number
            #accumulate teh poped values in a string cur
            elif c == ']':
                a = stack.pop()
                while isinstance(a, str):
                    cur = a + cur
                    a = stack.pop()

                # we must hit a number
                #duplicate cur string repetition based on number and push onto stack
                cur *= a
                stack.append(cur)

                cur = ""
             
            else:
                cur += c

        # join stack
        stack.append(cur)

        res = "".join(stack)
        return res


        # num = 
        #cur = bbbbbbbbb
        #stack = 3 a 
