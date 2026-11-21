class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        

        mp = defaultdict(list)

        sortedTuple = sorted(zip(timestamp, username, website))

        for a, b, c in sortedTuple:
            mp[b].append(c)

        tripletCount = defaultdict(int)
        for p in mp.keys():
            for i in range(len(mp[p])):
                for j in range(i + 1, len(mp[p])):
                    for k in range(j + 1, len(mp[p])):
                        tripletCount[mp[p][i], mp[p][j], mp[p][k]] += 1

        maxx = 0
        maxt, maxu, maxw = "", "", ""
        for (t, u, w), v in tripletCount.items():
            if (v > maxx
            or (v == maxx and ((t,u,w) < (maxt,maxu,maxw)))):
                maxx = v
                maxt, maxu, maxw = t, u, w

        return [maxt, maxu, maxw]
