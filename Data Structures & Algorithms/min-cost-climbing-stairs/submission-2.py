class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        memo = defaultdict(int)


        def dfs(x):

            def val(x):
                if x < 0:
                    return 0
                else:
                    return cost[x]

            if x < 0:
                return 0
            else:
                return min(dfs(x-1)+ val(x-1), 
                           dfs(x-2)+ val(x-2))

        return dfs(len(cost))
