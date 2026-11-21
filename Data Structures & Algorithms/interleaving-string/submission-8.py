class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        s_len = len(s1)
        t_len = len(s2)

        memo = defaultdict(bool)

        if s_len + t_len != len(s3):
            return False

        def dfs(s_i, t_i):

            if s_i == s_len and t_i == t_len:
                return True


            if (s_i, t_i) in memo:
                return memo[(s_i, t_i)]

            if s_i < s_len and s1[s_i] == s3[s_i + t_i]:
                memo[(s_i, t_i)] = memo[(s_i, t_i)] or dfs(s_i+1, t_i)

            if t_i < t_len and s2[t_i] == s3[s_i + t_i]:
                memo[(s_i, t_i)] = memo[(s_i, t_i)] or dfs(s_i, t_i+1)

            return memo[(s_i, t_i)]


        return dfs(0, 0)