class Solution:
    def checkValidString(self, s: str) -> bool:
        
        

        leftMax, leftMin = 0, 0

        for c in s:
            if c == '(':
                leftMax += 1
                leftMin += 1
            elif c == ')':
                leftMax -= 1
                leftMin -= 1
            else:
                leftMax += 1
                leftMin -= 1

            if leftMax < 0:
                return False

            leftMin = max(leftMin, 0)
            
        if leftMin <= 0 and leftMax >= 0:
            return True
        else:
            return False