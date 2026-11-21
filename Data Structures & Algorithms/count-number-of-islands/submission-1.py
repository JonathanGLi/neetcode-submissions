class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #checks if coordinates are in bounds
        def inBounds(i, j):
            if (i >= 0) and (i < len(grid)) and (j >= 0) and (j < len(grid[0])):
                return True
            return False

        def markBFS(starting_i, starting_j):
            
            #marks grid as 2 if it is a 1
            if (grid[starting_i][starting_j] == "1"):
                grid[starting_i][starting_j] = "2"

                #recursively calls each direction
                if inBounds(starting_i, starting_j-1):
                    markBFS(starting_i, starting_j-1)
                if inBounds(starting_i-1, starting_j):
                    markBFS(starting_i-1, starting_j)
                if inBounds(starting_i, starting_j+1):
                    markBFS(starting_i, starting_j+1)
                if inBounds(starting_i+1, starting_j):
                    markBFS(starting_i+1, starting_j)

        
        counter = 0

        # loop through each index
        for i in range(len(grid)):
            for j in range(len(grid[0])):

            # when find 1
                if grid[i][j] == "1":
                # do bfs and mark 1's as 2's
                    markBFS(i, j)

                    #   update counter  
                    counter+=1

        return counter




