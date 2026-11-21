class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        sett = set()

        #loop thorugh list
        #while char in set, move left pointer up and remove it from set
        #take max len every time char is added to set

        maxlen = 0

        i, j = 0, 0

        for j in range(len(s)):
            c = s[j]

            while c in sett:
                sett.remove(s[i])
                i+= 1

            sett.add(c)
            
            maxlen = max(maxlen, j - i + 1)

        return maxlen

