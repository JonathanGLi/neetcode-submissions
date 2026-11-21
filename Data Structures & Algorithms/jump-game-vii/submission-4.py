from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        

        q = deque([0])
        farthest = 0

        while q:
            i = q.popleft()

            start = max(i + minJump, farthest)

            for j in range(start, min(maxJump + i+1, len(s))):
                if j == len(s)-1:
                    return s[j] == '0'
                if s[j] == '0':
                    q.append(j)

            farthest = maxJump + i

        return False





