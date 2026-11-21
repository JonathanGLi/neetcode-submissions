import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # k/hour
        # h hours
        #binary search, try k then change k then try k 
        # binary search but instead of comparison we check if k-1 doesn't workk and k works
        #t = total bananas
        #m max number of bananas in any pile
        #t log(m)
        n = len(piles)
        l = 0

        r = 1
        for x in piles:
            r = max(r, x)

        # returns -1, 0, 1
        # worst case time
        def valid(pot_k):
            counted_hours = 0
            for bananas in piles:
                counted_hours += math.ceil(bananas/pot_k)

            counted_hours_ob = 0
            if (pot_k > 1):
                for bananas_ob in piles:
                    counted_hours_ob += math.ceil(bananas_ob/(pot_k-1))

            print(counted_hours)
            if (counted_hours <= h and ((counted_hours_ob > h) or pot_k == 1)):
                print("hi")
                print(counted_hours)
                print(h)
                return 0
            elif (counted_hours <= h and ((counted_hours_ob <= h) or pot_k == 1)):
                return -1
            else:
                return 1

            
        # binary seacrh
        while (l <= r):
            m = (l+r)//2
            dirr = valid(m)

            if dirr == 0:
                return int(m)
            elif dirr == -1:
                r = m-1
            else:
                l = m+1


