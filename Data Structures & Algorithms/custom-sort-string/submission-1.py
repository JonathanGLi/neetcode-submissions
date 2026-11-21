class Solution:
    def customSortString(self, order: str, s: str) -> str:
        

        count = 26 * [0]

        for c in s:
            count[ord(c) - ord('a')]+=1

        res = []
        for c in order:
            i = ord(c) - ord('a')
            while count[i] > 0:
                res.append(c)
                count[i] -=1

        for i in range(26):
            while count[i] > 0:
                res.append(chr(ord('a') + i))
                count[i] -=1

        return "".join(res)
        


