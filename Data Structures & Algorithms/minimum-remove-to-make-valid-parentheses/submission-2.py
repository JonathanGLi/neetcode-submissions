class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        

        openCount = closeCount = 0
        for c in s:
            if c == ')':
                closeCount +=1

        res = ""
        for c in s:


            if c == '(':
                if openCount == closeCount:
                    continue
                openCount += 1
            elif c == ')':
                closeCount -=1
                if openCount == 0:
                    continue
                openCount -= 1

            
            res += c

        return res





































        # count = 0
        # res = ''
        # for i in s:
        #     if i == ')': 
        #         if count > 0: 
        #             res += ')'
        #             count -= 1
        #     elif i == '(': 
        #         count += 1
        #         res += i
        #     else: 
        #         res += i
        
        # while count > 0:

        #     for i, char in enumerate(res[::-1]):
        #         if char == '(':
        #             res = res[:len(res)-i-1] + res[(len(res)-i):]
        #             count -= 1

        
        # return res
        

