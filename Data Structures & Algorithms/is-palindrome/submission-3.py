class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and (self.alphaNum(s[left]) == False):
                left+=1
            while left < right and (self.alphaNum(s[right]) == False):
                right-=1
            if left >= right:
                break

            print(s[left] + " " + s[right])

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))