class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = defaultdict(int)
        n = len(coins)

        # starting from this index, and with this total(cur amount), 
        # how many ways are there to get to amount
        def dfs(i, total):

            #bc
            if total == amount:
                return 1
            elif total > amount:
                return 0

            if i >= n:
                return 0

            #memo
            if (i, total) in memo:
                return memo[(i, total)]

            # stay
            memo[(i, total)] += dfs(i, total + coins[i])

            # move
            memo[(i, total)] += dfs(i+1, total)

            return memo[(i, total)]

        return dfs(0, 0)

        #0, 0
        #0, 1
        #0, 2
        #0, 3
        #0, 4   +1
        #1, 3   dead end







