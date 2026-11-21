class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        sum = 0
        for m in matchsticks:
            sum += m

        if (sum%4 != 0):
            return False

        side = sum / 4

        sorted_m = sorted(matchsticks)

        sides = [0]* 4


        def dfs(i):
            if i == -1:
                return True

            for j in range(4):           
                if sorted_m[i] + sides[j] <= side:
                    sides[j] += sorted_m[i]
                    if dfs(i-1) == True:
                        return True

                    sides[j] -= sorted_m[i]
                    

            return False

        return dfs(len(matchsticks)-1)


