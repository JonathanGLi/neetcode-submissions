class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:


        def works(size):
            cur = 0
            buckets = k

            print("size", size)
            for n in nums:
                print("n", n)
                if n + cur > size:
                    buckets -= 1
                    if buckets == 0:
                        return False
                    cur = n
                    print("a")

                else:
                    cur += n
                    print('b')
            return True



        l, r = max(nums), sum(nums)
        
        res = r

        while (l<=r):
            m = (l+r)//2
            print(m)

            if works(m):

                r= m-1
                res = m
            else:
                l = m+1

        return res
