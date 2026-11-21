class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        

        stack = []

        #for each astroid
        for a in asteroids:

            # if negative, and top is a smaller keep destroying 
            while stack and a < 0 and stack[-1] > 0 and abs(a) > abs(stack[-1]):
                stack.pop()

            # if negative, and top is a bigger + then dont push, ast gets destroid
            if stack and a < 0 and stack[-1] > 0 and abs(a) == abs(stack[-1]):
                stack.pop()
                continue

            elif stack and a < 0 and stack[-1] > 0 and abs(a) < abs(stack[-1]):
                continue

            #if + then continue
            else:
                stack.append(a)

        return stack
