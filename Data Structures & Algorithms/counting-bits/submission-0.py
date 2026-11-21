class Solution:
    def countBits(self, n: int) -> List[int]:

        # 0 1 2 3 4 5 6 7 8 9 
        # 0 1 1 2 1 2 2 3 4 2 

        arr= [0 for i in range (n+1)]

        offset = 1
        for i in range(1, n+1):

            if 2*offset == i:
                offset *= 2

            arr[i] = 1 + arr[i - offset]


        return arr

            




            

    