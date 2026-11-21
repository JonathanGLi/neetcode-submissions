class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        D = dict()
        biggestDiff = 0
        diff = 0

        beenTo = set()

        # loop thorugh nums
        for n in nums:
            if n not in beenTo:
                beenTo.add(n)

                if n-1 in D and n+1 in D:
                    a1, b1 = D[n-1]
                    a2, b2 = D[n+1]
                    D[a1] = (a1, b2)
                    D[b2] = (a1, b2)
                    diff = b2 - a1 + 1
                    print("-(" + str(a1) + ", " + str(b2) +")-")
                    
                elif n-1 in D:
                    a, b = D[n-1]
                    D[a] = (a, n)
                    D[n] = (a, n)
                    diff = n - a + 1
                    print("-(" + str(a) + ", " +str(n) +")-")

                elif n+1 in D:
                    a, b = D[n+1]
                    D[n] = (n, b)
                    D[b] = (n, b)
                    diff = b - n + 1
                    print("-(" + str(n) + ", " +str(b) +")-")
                else:
                    D[n] = (n, n)
                    diff = 1
                    print("-(" + str(n) + ", "+ str(n) + ")-")

                if diff> biggestDiff:
                    biggestDiff = diff

        return biggestDiff

