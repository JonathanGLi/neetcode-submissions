class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        #bs

        #avg - total

        def works(size):

            count = 1
            cur = 0
            for n in nums:
                if cur + n > size:
                    count += 1
                    cur = 0
                cur += n

            if count <= k:
                return True
            else:
                return False


        n = len(nums)

        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            print(l, r)

            m = (l + r) // 2
            print(m)

            if works(m):
                res = m
                r = m - 1
            else:
                l = m + 1

        print(works(16))
        return res


