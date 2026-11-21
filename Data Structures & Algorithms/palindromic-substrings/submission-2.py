class Solution:
    def countSubstrings(self, s: str) -> int:
        

        res = 0

        for i in range(len(s)):
            j, k = i, i
            while j >= 0 and k < len(s):
                if s[j] == s[k]:
                    res +=1
                else:
                    break
                j -= 1
                k += 1

        for i in range(len(s)-1):
            j, k = i, i+1
            while j >= 0 and k < len(s):
                if s[j] == s[k]:
                    res +=1
                else:
                    break
                j -= 1
                k += 1

        return res


