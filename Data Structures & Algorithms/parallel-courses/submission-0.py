class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        

        child_map = defaultdict(list)
        for p, c in relations:
            child_map[p].append(c)

        memo = {}

        def dfs(i):

            if i in memo:
                return memo[i]
            if i in visited:
                return -1

            visited.add(i)

            res = 0
            for child in child_map[i]:
                val = dfs(child)
                if val == -1:
                    return -1
                res = max(res, val+1)

            memo[i] = res

            return res


        res = 0
        for i in range(1, n+1):
            visited = set()
            val = dfs(i)
            print(val)
            if val == -1:
                return -1
            res = max(res, val)

        return res+1



