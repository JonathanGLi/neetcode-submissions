class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        

        noAddSet = set()
        openCount = closedCount = 0
        count = 0

        for i in range(len(s)):

            c = s[i]
            if c == '(':
                openCount+=1
                count += 1
            if c == ')':
                if count > 0:
                    closedCount += 1
                    count -= 1
                else:
                    noAddSet.add(i)

        #
        print(openCount)
        print(closedCount)
        
        count1 = 0

        openCount = min(openCount, closedCount)
        closedCount = openCount

        res = ""
        for i in range(len(s)):
            if s[i] == '(':
                if openCount > 0:
                    openCount-=1                
                    res += s[i]
            elif s[i] == ')':
                if closedCount > 0 and i not in noAddSet:
                    closedCount-=1
                    res += s[i]
            else:
                res += s[i]

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
        

