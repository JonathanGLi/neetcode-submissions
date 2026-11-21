class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longestString = ""
        longest = 0
        index = 0

        while index < len(s):

            curLen = 1

            i = index
            j = i
            while (i >= 0 and j < len(s) and s[i] == s[j]):
                if i!= j:
                    curLen +=2
                if curLen > longest:
                    longest = curLen
                    longestString = s[i:j+1]
                i-=1
                j+=1

            if index >= len(s)-1:
                break
            print("hi")
            print(index)
            curLen = 2
            i = index
            j = i+1
            while (i >= 0 and j < len(s) and s[i] == s[j]):
                if j != i+1:
                    curLen +=2
                if curLen > longest:
                    longest = curLen
                    longestString = s[i:j+1]
                i-=1
                j+=1

            index += 1

        return longestString

