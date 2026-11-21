class Solution:
    def minWindow(self, s: str, t: str) -> str:

        lenShortestSub = len(s)
        shortestSub = ""

        refD, D = {}, {}

        for c in t:
            print("c: " + c)
            refD[c] = 1+refD.get(c, 0)

        print("refD: ", refD)

        have, need = 0, len(refD)
        l = 0

        for r in range(len(s)):

            print("D: ", D)

            D[s[r]] = D.get(s[r], 0) + 1
            if s[r] in refD and D[s[r]] == refD[s[r]]:
                print("have: ", str(have))
                print("need: ", str(need))
                have += 1

                while have == need:
                    print("aa")
                    if (r-l+1 <= lenShortestSub):
                        print("sss")
                        lenShortestSub = r-l+1
                        shortestSub = s[l:r+1]

                    if s[l] in refD and D[s[l]] == refD[s[l]]:
                        have -= 1
                    D[s[l]] -= 1
                    l+=1
                    
                    
        return shortestSub


