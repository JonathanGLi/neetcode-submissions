class Solution:
    def simplifyPath(self, path: str) -> str:

        cur = ""
        n = len(path)
        stack = []

        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != "." and cur != "":
                    stack.append(cur)
                cur = ""
            else:
                cur += c

        print(stack)


        return "/" + "/".join(stack)




        