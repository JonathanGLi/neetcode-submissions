class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        x1 = x

        rev = 0

        while x1 > 0:

            m = x1 % 10
            x1 = x1//10

            rev *= 10
            rev+= m

        return rev == x