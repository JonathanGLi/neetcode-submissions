class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        

        i, j = 0, 0

        res = ""

        for i in range(min(len(word1), len(word2))):
            res += word1[i]
            res += word2[i]

        i+=1

        if len(word1) > len(word2):
            res += word1[i:len(word1)]
        elif len(word2) > len(word1):
            res += word2[i:len(word2)]

        return res