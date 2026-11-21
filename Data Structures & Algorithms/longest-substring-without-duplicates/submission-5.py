class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        
        i = 0
        j = i
        sett = set()
        longestLen = 0

        while (j < len(s)):

            while s[j] in sett:

                sett.remove(s[i])
                
                i+=1

            sett.add(s[j])

            length = j - i
            longestLen = max(longestLen, length)

            j+=1

        return longestLen+1

