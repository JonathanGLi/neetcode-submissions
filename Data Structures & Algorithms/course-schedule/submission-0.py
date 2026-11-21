class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # create a tree, 

        #prereq => course
        mp = defaultdict(list)
        for c, pre in prerequisites:
            mp[pre].append(c)

        visited = set()
        visitedThisIter = set()
        cycle = [False]

        def dfs(c):

            if c in visited:
                if c in visitedThisIter:
                    cycle[0] = True
                return 
            visited.add(c)
            visitedThisIter.add(c)
            for course in mp[c]:
                dfs(course)


        for c in range(numCourses): 
            visitedThisIter = set()
            dfs(c)

        print(len(visited))

        if cycle[0] == True:
            return False

        if len(visited) == numCourses:
            return True

        return False

