class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        nLen = len(needle)
        ps = [0] * nLen
        p, i = 0, 1

        while i < nLen:
            if needle[p] == needle[i]:
                ps[i] = ps[i-1] + 1
                p += 1
                i += 1
            elif p == 0:
                ps[i] = 0
                i += 1
            else:
                p = ps[p-1]
        print(ps)
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j +=1 
            elif j==0:
                i+=1
            else:
                j = ps[j-1]

            if j == len(needle):
                return i - len(needle)

        return -1



        # if needle == "": return 0
        # lps = [0] * len(needle)

        # prevLPS, i = 0, 1
        # while i < len(needle):
        #     if needle[i] == needle[prevLPS]:
        #         lps[i] = prevLPS + 1
        #         prevLPS += 1
        #         i += 1
        #     elif prevLPS == 0:
        #         lps[i] = 0
        #         i += 1
        #     else:
        #         prevLPS = lps[prevLPS - 1]
        
        # print(lps)


        # i = 0  # ptr for haystack
        # j = 0  # ptr for needle
        # while i < len(haystack):
        #     if haystack[i] == needle[j]:
        #         i, j = i + 1, j + 1
        #     else:
        #         if j == 0:
        #             i += 1
        #         else:
        #             j = lps[j - 1]

        #     if j == len(needle):
        #         return i - len(needle)

        # return -1


