class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        

        people.sort()
        count = 0
        l, r = 0, len(people)-1

        while r >= 0 and people[r] == limit:
            r-=1
            count += 1


        while (l < r):

            if (people[l] + people[r]) > limit:
                r-=1
            else:
                l +=1
                r -= 1

            count +=1

        if l == r:
            count+=1

        return count

        #1 2 2 3 3 
        #1 2 2 
