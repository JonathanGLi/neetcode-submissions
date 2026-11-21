class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        #create presreq treee


        preReqList = [[] for i in range( numCourses)]

        for u, v in prerequisites:
            preReqList[v].append(u)


        #create prereqmap
        def dfs(course):
            if course not in prereqmap:
                prereqmap[course].add(course)
                for c in preReqList[course]:
                    prereqmap[course] |= dfs(c)
            return prereqmap[course]

        prereqmap = defaultdict(set)
        for i in range(numCourses):
            dfs(i)


        return [u in prereqmap[v] for u, v in queries]

        