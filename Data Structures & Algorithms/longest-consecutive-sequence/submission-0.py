class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        D = {}
        maxlen = 0
        up = 1
        down = -1
        l = 0

        for n in nums:
            if (n, up) not in D:
                if ((n-1, down) not in D) and ((n+1, up) not in D):
                    D[(n, down)] = 1
                    D[(n, up)] = 1
                    l = 1
                    print(l)
                elif ((n-1, down) in D) and ((n+1, up) not in D):
                    D[(n, down)] = D[(n-1, down)] + 1
                    D[(n - D[(n-1, down)], up)] = D[(n-1, down)] + 1
                    l = D[(n-1, down)] + 1
                elif ((n-1, down) not in D) and ((n+1, up) in D):
                    D[(n + D[(n+1, up)], down)] = D[(n+1, up)] + 1
                    D[(n, up)] = D[(n+1, up)] + 1
                    l = D[(n+1, up)] + 1
                elif ((n-1, down) in D) and ((n+1, up) in D):
                    D[(n + D[(n+1, up)], down)] = D[(n-1, down)] + D[(n+1, up)] + 1
                    D[(n - D[(n-1, down)], up)] = D[(n-1, down)] + D[(n+1, up)] + 1
                    l = D[(n-1, down)] + D[(n+1, up)] + 1

                if l > maxlen:
                    maxlen = l

        return maxlen