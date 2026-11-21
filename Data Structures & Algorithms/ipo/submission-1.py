class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        




        # sort (profits, captital) array largest profits first

        # k times
        # find the largest profit you acan affor 


        # k * n, 

        sortt = sorted([(profits[i], capital[i]) for i in range(len(capital))], reverse = True)
        cap = w
        seen = set()
        print(sortt)
        for i in range(k):


            j = 0
            while j < len(sortt) and sortt[j][1] > cap or j in seen:
                j += 1

            if j == len(sortt):
                return cap

            print(j)

            cap += sortt[j][0]
            seen.add(j)
            print(cap, seen)


        return cap

            

