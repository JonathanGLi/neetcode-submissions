class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        if len(nums) == 0:
            return 0
        
        d = {}

        max = 0


        for n in nums:

            print(n)
            
            if n+1 in d and n-1 in d:
                start = d[n-1]
                end = d[n+1]
                d[d[n-1]] = end
                d[d[n+1]] = start
                print(d)
                if (end - start) > max:
                    max = (end - start)

                if d[n+1]!= start:
                    del d[n+1]
                if n in d:
                    del d[n]
                if d[n-1]!= end:
                    del d[n-1]


            elif n+1 in d:
                if d[n+1] > n:
                    d[n] = d[n+1]
                    d[d[n+1]] = n
                    if ((d[n] - n) > max):
                        max = (d[n] - n)

                    if d[n+1]!= n:
                        del d[n+1]

            elif n-1 in d:
                if d[n-1] < n:
                    d[n] = d[n-1]
                    d[d[n-1]] = n
                    if (n - d[n]) > max:
                        max = (n - d[n])
                    if d[n-1]!= n:
                        del d[n-1]

            elif n not in d:
                d[n] = n

            print(d)

        return max+1