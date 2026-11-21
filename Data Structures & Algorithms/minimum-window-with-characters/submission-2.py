class Solution:
    def minWindow(self, s: str, t: str) -> str:

        lenShortestSub = len(s)
        shortestSub = ""

        #creating 2 arrays
        refArray = [0] * 80
        Array = [0] * 80

        #filling in the ref array
        for c in t:
            refArray[ord(c) - ord("A")] += 1

        print("refArray: ", refArray)

        #making 2 pointers
        l, r = 0, 0

        Array[ord(s[r]) - ord("A")] += 1

        #loop traversal 
        while r != len(s):
            
            #while the substring does not contain the letters, expand the substring to the right
            #
            while (self.containsLetters(Array, refArray) == False):
                r+=1
                print("r: " + str(r))
                if r == len(s):
                    break
                Array[ord(s[r]) - ord("A")] += 1
                print("Array: ", Array)


            while (self.containsLetters(Array, refArray) == True):


                if (r-l+1 <= lenShortestSub):
                    lenShortestSub = r-l+1
                    shortestSub = s[l:r+1]
                    print("shortestSub: " + shortestSub)


                print("l: " + str(l))
                Array[ord(s[l]) - ord("A")] -= 1
                l+=1


        return shortestSub


    def containsLetters(self, a1, a2):
        for i in range(len(a1)):
            if a1[i] < a2[i]:
                return False

        return True
