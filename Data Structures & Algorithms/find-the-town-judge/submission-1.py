class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # E, E
        # create adj list

        # loop through edges and find o

        #loop through edges, count the number of edges that map to a certain node
        mapp = defaultdict(int)

        for a, b in trust:
            mapp[b] += 1
            mapp[a] = -float('inf')

        for i in range(1, n+1):
            if mapp[i] == n-1:
                return i

        return -1
            

