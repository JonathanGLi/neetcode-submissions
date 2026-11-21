class Solution:
    def decodeString(self, s: str) -> str:
        

        stack = []

        for i in range(len(s)):
            print(stack)

            if s[i] != ']':
                stack.append(s[i])

            else:
                #build cur
                cur = ""
                a = stack.pop()
                while a != "[":
                    cur = a + cur
                    a = stack.pop()

                # build number
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * cur)

        return "".join(stack)

                #multiply
