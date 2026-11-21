class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = defaultdict(list)
        for prereq, crs in prerequisites:
            adj[crs].append(prereq)

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for prereq in adj[crs]:
                    prereqMap[crs] |= dfs(prereq)
                prereqMap[crs].add(crs)
            return prereqMap[crs]

        prereqMap = {}
        for crs in range(numCourses):
            dfs(crs)

        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        return res
        # #create presreq treee


        # preReqList = [[] for i in range( numCourses)]

        # for u, v in prerequisites:
        #     preReqList[v].append(u)


        # #create prereqmap
        # def dfs(course):
        #     prereqmap[course].add(course)
        #     for c in preReqList[course]:
        #         prereqmap[course] |= dfs(c)
        #     return prereqmap[course]

        # prereqmap = defaultdict(set)
        # for i in range(numCourses):
        #     dfs(i)


        # return [u in prereqmap[v] for u, v in queries]

        