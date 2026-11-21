class Solution:
    def countPrimes(self, n: int) -> int:

        isPrime = [True] * n
        res = 0

        for i in range(2, n):
            if isPrime[i]:
                res += 1
                for j in range(i*i, n, i):
                    isPrime[j] = False

        return res