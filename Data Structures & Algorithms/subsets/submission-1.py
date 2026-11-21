class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        


        # empty list
        res = [[]]

        # 
        for n in nums:

            print(n, res)

            temp = []

            for i in range(len (res)):

                #add or not add
                #add both version to list
                # doubles each iteration
                print(res[i])
                temp.append(res[i].copy())
                res[i].append(n)
                temp.append(res[i])

                print("temp", temp)

            res = temp

        return res

