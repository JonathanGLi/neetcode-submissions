class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]
        
        # each tree
        # find the height of that tree

        node_count = n
        #maps node -> edge count

        adj_list = defaultdict(set)

        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)


        q = deque([])

        for node, neighbors in adj_list.items():
            if len(neighbors) == 1:
                q.append(node)

        while node_count > 2 and q:
            for i in range(len(q)):
                u = q.popleft()
                v = list(adj_list[u])[0]

                adj_list[u].remove(v)
                adj_list[v].remove(u)

                node_count-=1   

                if len(adj_list[v]) == 1:
                    q.append(v)

        return list(q)





                














        