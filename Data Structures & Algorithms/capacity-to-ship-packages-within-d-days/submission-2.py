class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        


        def canCap(cap):
            curCap = 0
            d = 1
            for w in weights:
                if curCap + w > cap:
                    curCap = 0
                    d += 1
                curCap += w
                if curCap > cap:
                    return False
            if d > days:
                return False
            return True




        l, r = max(weights), sum(weights)
        res = sum(weights)
        while l<= r:
            m = (l + r)//2

            if canCap(m):
                res= min(res, m)
                r = m-1

            else:
                l = m + 1

        return res