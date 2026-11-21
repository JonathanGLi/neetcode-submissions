class UnionFind:

    def __init__(self, size):
        self.parent = [-1] * size
        self.rank = [0] * size
        self.count = 0

    def numIslands(self) -> int:
        return self.count

    def find(self, x) -> int:
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])

    def union(self, x, y) -> None:

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1 

        self.count -= 1

        return





class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        xy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        uf = UnionFind(m*n)
        res = []

        for (i, j) in positions:
            print("||||||||||||||||")
            pos = n * i + j

            # if seen
            if uf.parent[pos] != -1:
                res.append(uf.numIslands())
                continue

            uf.parent[pos] = pos
            uf.count += 1

            for (x, y) in xy:
                # print(i, j)
                # print(x, y)
                # print(i+x, j + y)
                pos1 = n * (i+x) + (j + y)
                # print("pos1", pos1)
                if (i+x >= 0
                and i+x < m
                and j+y >= 0
                and j+y < n
                and uf.parent[pos1] != -1):

                    uf.union(pos1, pos)
                    # print("union", pos1, pos)

            res.append(uf.numIslands())

            # print(uf.parent)
            # print("pos", pos)
            # print("uf.count", uf.count)

        return res


        









        