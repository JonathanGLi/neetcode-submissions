class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.size = [0] * n
        self.count = n

    def getParlist(self):
        return self.par

    def getpar(self, i):
        if self.par[i] == i:
            return i
        else:
            self.par[i] = self.getpar(self.par[i])

        return self.par[i]


    def union(self, i, j):

        p1, p2 = self.getpar(i), self.getpar(j)

        if p1 == p2:
            return

        self.count -= 1
        if self.size[p1] > self.size[p2]:
            self.size[p1] += self.size[p2]
            self.par[p2] = p1
        else:
            self.size[p2] += self.size[p1]
            self.par[p1] = p2


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        
        n = len(nums)

        if 1 in nums:
            return False
        if n == 1:
            return True

        uf = UnionFind(n)

        #Seave
        # maps each num to its smallest prime factor
        MAX = max(nums) + 1
        seave = list(range(MAX))
        for i in range(2, int(MAX**0.5)+1):
            if seave[i] == i:
                for j in range(i*i, MAX, i):
                    if seave[j] == j:
                        seave[j] = i

        #loop through

        map_primes_to_i = {}

        count = 0
        for i, val in enumerate(nums):
            while val > 1:
                smallest_prime_factor = seave[val]

                # print(val, smallest_prime_factor)

                # count += 1
                # if count == 10:
                #     print("ahhh")
                #     return True
                if smallest_prime_factor in map_primes_to_i:
                    uf.union(i, map_primes_to_i[smallest_prime_factor])
                else:
                    map_primes_to_i[smallest_prime_factor] = i
                while val % smallest_prime_factor == 0:
                    val //= smallest_prime_factor

        return uf.count == 1


















        