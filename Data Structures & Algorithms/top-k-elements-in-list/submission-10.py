class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #key is the number
        #value is the number it shows up
        D = defaultdict(int)
        for n in nums:
            D[n] += 1

        #array
        #index is the number of times a number shows up
        #value is the list of numbers
        #max length is number of numbers in the original array
        array = [[] for i in range(len(nums)+1)]

        for key, v in D.items():
            array[v].append(key)

            print("Key: " + str(key) + "Key: " + str(v))



        #resulting array is formed by looping through above array from the back
        #popping off the last k 
        res = []
        kC = k

        print("START kC: " + str(kC))

        for i in range(len(nums), 0, -1):

            print("i: " + str(i))
            print("len(array[i]: " + str(len(array[i])))
            
            while (len(array[i]) != 0 and kC != 0):

                res.append(array[i].pop())
                kC-=1

            print("kC: " + str(kC))

        return res