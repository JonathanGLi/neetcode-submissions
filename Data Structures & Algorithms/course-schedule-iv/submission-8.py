class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        

        # loop through every uj
        # run dfs staring from every uj =, if we find vj then true else false
        adjList = [[]for i in range(numCourses)]
        for u, v in prerequisites:
            adjList[u].append(v)

        memo ={}
        def dfs(uj, vj):
            if (uj, vj) in memo:
                return memo[(uj, vj)]
            
            if uj == vj:
                memo[(uj, vj)] = True
                return True
            for child in adjList[uj]:
                if dfs(child, vj):
                    memo[(uj, vj)] = True
                    return True
            memo[(uj, vj)] = False
            return False


        
        res = []
        for uj, vj in queries:

            res.append(dfs(uj, vj))


        return res
