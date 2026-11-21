class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        

        letters_s = 26 * [0]
        letters_t = 26 * [0]

        for c in s:
            letters_s[ord(c) - ord('a')] += 1

        for c in t:
            letters_t[ord(c) - ord('a')] += 1

        for i in range (26):
            if letters_t[i] > letters_s[i]:
                return chr(ord('a') + i)