class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        # restate


        # questions
        # empty island?, no
        #at least one?, no

        #edge

        #2 implementaitons
        #dfs - 

        #loop over gird
        # if 1,  dfs from that point
        # modifu the 1 to be -1 to show already seen
        #count with dfs area
        # O(n * m) n = rows, m = cols


        #bfs

        #loop over gird
        # if 1, bfs from that point


        def bfs(i, j):
            

            count = 0

            # queue of island coords
            q = [(i, j)]

            #loop thorugh q
            for (i, j) in q:
                # in bounds
                if (i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])):
                    # modify the 1 to be -1 to show already seen
                    if grid[i][j] == 1:

                        grid[i][j] = -1

                        # increment counter
                        count += 1

                        #append adjacent coords with 1
                        q.append((i-1, j))
                        q.append((i+1, j))
                        q.append((i, j-1))
                        q.append((i, j+1))

            return count


        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islandSize = bfs(i, j)

                    res = max(res, islandSize)

        return res













