class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        

        parent = [i for i in range(n)]
        count = [1 for i in range(n)]

        def findRoot(i):
            while parent[i] != i:
                i = parent[i]

            return i

        for x, y in edges:
            a = findRoot(x)
            parent[x] = a

            b = findRoot(y)
            parent[y] = b

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
            




