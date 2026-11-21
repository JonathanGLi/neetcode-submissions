

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        
        if len(nums) == 1: return True
        if 1 in nums: return False # More than 1 element and one is '1'
        
        M = max(nums) + 1
        # 1. SPF Sieve
        spf = list(range(M))
        for i in range(2, int(M**0.5) + 1):
            if spf[i] == i:
                for j in range(i*i, M, i):
                    if spf[j] == j: spf[j] = i
        
        # 2. Union-Find on Indices
        n = len(nums)
        parent = list(range(n))
        count = n
        
        def find(i):
            if parent[i] == i: return i
            parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            nonlocal count
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                count -= 1

        # 3. Connect via Prime "Hubs"
        prime_to_index = {}
        for i, val in enumerate(nums):
            while val > 1:
                p = spf[val]
                if p in prime_to_index:
                    union(i, prime_to_index[p])
                else:
                    prime_to_index[p] = i
                while val % p == 0: val //= p # Standard log(n) factorization
                
        return count == 1