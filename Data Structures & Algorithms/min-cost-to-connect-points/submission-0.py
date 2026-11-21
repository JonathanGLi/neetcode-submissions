class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:



        # create adj list

        adjList = [[]for i in range(len(points))]

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))



        # prims
        mHeap = [[0, 0]]
        visited = set()
        res = 0

        while len(visited) < len(points):
            d, i = heapq.heappop(mHeap)
            if i in visited:
                continue
            res += d

            visited.add(i)

            for dist, j in adjList[i]:
                if j not in visited:
                    heapq.heappush(mHeap, [dist, j])

        return res
            
