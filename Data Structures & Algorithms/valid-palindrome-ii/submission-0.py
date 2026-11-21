class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrom(i, j):
            l, r = i, j

            while(l < r):
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True



        l, r = 0, len(s)-1


        while(l < r):
            if s[l] != s[r]:
                a = isPalindrom(l+1, r)
                b = isPalindrom(l, r-1)
                return a or b

            l+=1
            r-=1

        return True