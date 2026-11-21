class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = strs[0]
        for s in strs:

            i = 0
            while i < (min(len(res), len(s))):
                if res[i] != s [i]:

                    break
                i+=1

            res = res[:i]

        return res
