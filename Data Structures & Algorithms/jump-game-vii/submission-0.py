class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        

        windowCount = 0

        jumpable = [False] * len(s)
        jumpable[0] = True


        for i in range(1, len(s)):

            if i - minJump >= 0 and jumpable[i - minJump]:
                windowCount += 1

            if i - maxJump - 1 >= 0 and jumpable[i - maxJump - 1]:
                windowCount -= 1

            if s[i] == '1':
                continue
                
            if windowCount > 0:
                jumpable[i] = True

        print(jumpable)

        return jumpable[len(s) - 1]


