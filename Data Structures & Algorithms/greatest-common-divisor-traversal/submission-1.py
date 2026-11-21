class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        


        if 1 in nums:
            return False
        # union find

        # map indicies to sets of divisors
        # 4 => 2, 4
        # 3 => 3

        # 12 => 2, 3, 4, 6, 12

        primes = set()
        # larger primes to smaller primes
        edges_map = defaultdict(list)

        def isPrime(n):
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
            primes.add(n)
            return True


        def getPrimes(n):
            res = set()
            for i in range(2, n+1):
                if (n % i) == 0:
                    if isPrime(i): res.add(i)

            return res

        visited = set()
        def dfs(n):

            if n in visited:
                return 
            visited.add(n)
            for v in edges_map[n]:
                dfs(v)




                

        for n in nums:
            n_primes = list(getPrimes(n))

            for i in range(len(n_primes)-1):
                p1, p2 = n_primes[i], n_primes[i+1]
                edges_map[p2].append(p1)
                edges_map[p1].append(p2)

        print(primes)
        print(edges_map)


        dfs(list(primes)[0])
        return len(visited) == len(primes)



            












