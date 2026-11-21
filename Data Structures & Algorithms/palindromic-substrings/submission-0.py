class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0

        for index in range(len(s)):
            print(index)
            
            i = index
            #odd length
            j = i
            while i >=0 and j < len(s) and s[i] == s[j]:
                print("a")
                res += 1
                i-=1
                j+=1

            #even length
            i = index
            j = i+1
            while i >=0 and j < len(s) and s[i] == s[j]:
                print("b")
                res += 1
                i-=1
                j+=1

        return res