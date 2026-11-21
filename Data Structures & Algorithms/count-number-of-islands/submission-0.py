class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visit = set()

        def helper(r: int, c: int):

            if ((grid[r][c] == "1") and ((r, c) not in visit)):
                print("this helper", (r, c))

                visit.add((r, c))

                if ((r-1) >= 0):
                    helper(r-1, c)
                if ((c-1) >= 0):
                    helper(r, c-1)
                if ((r+1) < len(grid)):
                    helper(r+1, c)
                if ((c+1) < len(grid[r])):
                    helper(r, c+1)

            return

        islandCount = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                print((r, c))
                if ((grid[r][c] == "1") and ((r, c) not in visit)):
                    islandCount+=1
                    helper(r, c)
                print(islandCount)


        return islandCount
                
                