class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        

        def count(cur):

            res = 0
            nei = cur+1

            while cur <= n:

                res += min(nei, n+1) - cur
                cur *= 10
                nei *= 10

            return res


        cur = 1
        seen = 1

        while seen < k:
            c = count(cur)
            if k < seen + c:
                cur *=10
                seen += 1

            else:
                cur += 1
                seen += c

        return cur



