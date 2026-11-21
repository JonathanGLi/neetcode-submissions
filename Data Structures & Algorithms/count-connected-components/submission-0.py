class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        

        parent = [i for i in range(n)]
        count = defaultdict(int)

        def findRoot(i):
            while parent[i] != i:
                i = parent[i]

            return i

        for a, b in edges:
            a = findRoot(a)
            b = findRoot(b)

            #skip if same root
            if a == b:
                continue

            if count[a] > count[b]:
                parent[b] = a
                count[a] += count[b]
            else:
                parent[a] = b
                count[b] += count[a]

        count = 0
        for i in range(len(parent)):
            if parent[i] == i:
                count += 1
        return count
            




