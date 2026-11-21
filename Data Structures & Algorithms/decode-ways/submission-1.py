class Solution:
    def numDecodings(self, s: str) -> int:

        memo = defaultdict(int)
        

        def ways(strr):
            res = 0
            if strr == "":
                return 1
            if strr in memo:
                return memo[strr]
            #valid 1 digit
            if strr[0] == "0":
                return 0
            else:
                ways1 = ways(strr[1:])
                res += ways1
                memo[strr[1:]] = ways1

            #valid 2 digit
            if (len(strr) > 1 and (strr[0] == "1" or (strr[0] == "2" and (strr[1] == "0" or 
                strr[1] == "1" or 
                strr[1] == "2" or 
                strr[1] == "3" or 
                strr[1] == "4" or 
                strr[1] == "5" or
                strr[1] == "6")) )):
                ways2 = ways(strr[2:])
                res += ways2
                memo[strr[2:]] = ways2

            return res

        return ways(s)