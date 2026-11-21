class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        print("hi")


        mp_s = [0 for i in range(52)]
        mp_t = [0 for i in range(52)]

        for c in t:
            if c.isupper():
                mp_t[ord(c.lower()) - ord('a') + 26] += 1
            else:
                mp_t[ord(c.lower()) - ord('a')] += 1

        print("mp_t", mp_t)


        #O(1)
        def contains():
            for i in range(52):
                if mp_t[i] > mp_s[i]:
                    return False
            return True



        r = 0
        l = 0

        minLen = float('inf')
        minLenStr = (-1, -1)
        while r < len(s):

            if s[r].isupper():
                mp_s[ord(s[r].lower()) - ord('a') + 26] += 1
            else:
                mp_s[ord(s[r].lower()) - ord('a')] += 1

            r += 1
            while r < len(s) and not contains():
                if s[r].isupper():
                    mp_s[ord(s[r].lower()) - ord('a') + 26] += 1
                else:
                    mp_s[ord(s[r].lower()) - ord('a')] += 1
                r += 1

            print("r", r)
            
            if l < r-1 and contains():
                while l < r and contains():
                    if s[l].isupper():
                        mp_s[ord(s[l].lower()) - ord('a') + 26] -= 1
                    else:
                        mp_s[ord(s[l].lower()) - ord('a')] -= 1
                    l += 1
                l-=1
                if s[l].isupper():
                    mp_s[ord(s[l].lower()) - ord('a') + 26] += 1
                else:
                    mp_s[ord(s[l].lower()) - ord('a')] += 1

            print("mp_s", mp_s)

            if not contains():
                break

            curLen = r - l
            curStr = (l, r)

            if curLen < minLen:
                minLen = curLen
                minLenStr = curStr
                

        l, r = minLenStr
        if l == -1 and r == -1:
            return ""
        return s[l: r]


            


        
