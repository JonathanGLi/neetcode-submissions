class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        

        three = []
        xs = set()
        for i in range(len(x)):
            print("--"*3)
            print("three", three)
            print("x", xs)
            if len(three) < 3 and x[i] not in xs:

                three.append(i)
                xs.add(x[i])
            elif (x[i] in xs):

                for j in range (len(three)):
                    if x[three[j]] == x[i] and y[three[j]] < y[i]:
                        three[j] = i
            elif len(three) == 3: 
                min_y = y[three[0]]
                min_j = 0
                for j in range (len(three)):
                    if y[three[j]] < min_y:
                        min_y = y[three[j]]
                        min_j = j
                if min_y < y[i]:
                    xs.remove(x[three[min_j]])
                    three[min_j] = i
                    xs.add(x[i])

        if len(three) < 3:
            return -1

        print("sum", three)
        s = 0
        for j in (three):
            print(y[j])
            s += y[j]

        return s



            











































        #turn y into a maxheap (y, x), pop until we get 3 distinct