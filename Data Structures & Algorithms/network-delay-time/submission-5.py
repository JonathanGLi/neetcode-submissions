class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        #, n, n

        mapDist = {}

        m = defaultdict(list)
        for a, b, c in times:
            m[a].append((b, c))

        q = deque([(k, 0)])
        mapDist[k] = 0

        while q:
            (cur, cur_dist) = q.popleft()

            forward = m[cur]

            for f, d_dist in forward:
                if f not in mapDist or cur_dist + d_dist < mapDist[f]:
                    mapDist[f] = cur_dist + d_dist
                    q.append((f, cur_dist + d_dist))


        if len(mapDist) < n:
            return -1

        return max(mapDist.values())
