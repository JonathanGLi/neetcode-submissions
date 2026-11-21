class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        

        d = {}

        def dfs(i, j):

            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if (i, j) in d:
                return d[(i, j)]

            if word1[i] == word2[j]:
                d[(i, j)] = dfs(i+1, j+1)
                return d[(i, j)]

            best = float("inf")

            best = min(best, dfs(i+1, j))
            best = min(best, dfs(i, j+1))
            best = min(best, dfs(i+1, j+1))

            d[(i, j)] = best+1

            return d[(i, j)]
        print(d)
        return dfs(0, 0)