class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        #RQE2

        #What to do if there are ties, smae price, smae length, same price diff lenth
        # is this a DAG

        #BFS

        #djikstras


        #start location => [(endlocation1, cost1), (endlocation2, cost2)]
        neighbors = defaultdict(list)
        for f in flights:
            neighbors[f[0]].append((f[1], f[2]))

        #heap, (cheapest path to that node, node, depth of that node)
        frontier = []

        #put inital frontier
        for n in neighbors[src]:
            heapq.heappush(frontier, (n[1], n[0], 1))

        #maps node => cheapest path to that node
        visited = {}
        visited[src] = 0

        #pop cheapest from heap, cheapest path from root to that edge
        while frontier:

            pathCost, node, depth = heapq.heappop(frontier)


            #add that vertxex to visited
            if node in visited:
                visited[node] = min(pathCost, visited[node])
            else:
                visited[node] = pathCost

            # add its neighbors to frontier, only if they are within k+1 from the root
            if depth <= k:
                for n, cost in neighbors[node]:
                    heapq.heappush(frontier, (pathCost + cost, n, depth + 1))

        if dst not in visited:
            return -1
        return visited[dst]

                















