class Solution:
    def isValid(self, s: str) -> bool:
        


        stack = []

        for p in s:
            if (p == '(' or p == '[' or p == '{'):
                stack.append(p)
            elif (len(stack) == 0):
                return False
            else:
                x = stack.pop()
                if (p == ')' and not (x == '(')):
                    return False
                if (p == ']' and not (x == '[')):
                    return False
                if (p == '}' and not (x == '{')):
                    return False

        return len(stack) == 0