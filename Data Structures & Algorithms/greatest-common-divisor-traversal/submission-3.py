
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.components = n

    def getPar(self, i):
        if self.par[i] != i:
            self.par[i] = self.getPar(self.par[i])
        return self.par[i]

    def union(self, i, j):

        p1, p2 = self.par[i], self.par[j]

        if p1 == p2:
            return 
        self.components -=1

        if self.size[p1] < self.size[p2]:
            self.size[p2] += self.size[p1]
            self.par[p1] = p2
        else:
            self.size[p1] += self.size[p2]
            self.par[p2] = p1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        
        n = len(nums)

        uf = UnionFind(n)

        map_f_to_i = {}

        for i, val in enumerate(nums):
            f = 2
            while f**2 <= val:
                if val % f == 0:
                    if f in map_f_to_i:
                        uf.union(i, map_f_to_i[f])
                    else:
                        map_f_to_i[f] = i
                    while val % f == 0:
                        val /= f

                f += 1
            if val > 1:
                if val in map_f_to_i:
                    uf.union(i, map_f_to_i[val])
                else:
                    map_f_to_i[val] = i

        return uf.components == 1
                







