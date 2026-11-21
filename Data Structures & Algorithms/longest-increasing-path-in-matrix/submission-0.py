class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        dp = defaultdict(list)


        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            val = matrix[i][j]
            res = 1

            if i-1>=0 and matrix[i-1][j] >  val:
                res = max(res, 1 + dfs(i-1, j))
            if j-1>=0 and matrix[i][j-1] >  val:
                res = max(res, 1 + dfs(i, j-1))
            if i+1<len(matrix) and matrix[i+1][j] >  val:
                res = max(res, 1 + dfs(i+1, j))
            if j+1<len(matrix[0]) and matrix[i][j+1] >  val:
                res = max(res, 1 + dfs(i, j+1))

            dp[(i, j)] = res
            return res

        maxx = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                maxx = max(maxx, dfs(i, j))

        return maxx

