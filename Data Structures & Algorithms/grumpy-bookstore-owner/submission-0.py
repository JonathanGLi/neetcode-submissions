class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        #RQE2


        # find the largest subseq mask sum value

        #Q
        # can customer list be shorter thatn the minutes
        #no neg customers
        #can min be 0, yes

        #for each stading index of the window, calcuate teh sum, glob max 
        #n*2

        #sliding
        #n
        # subtract left
        #l+=1, r+=1
        #summ += grumpy[i] * customers[i]
        # max it 
        # keep track of window start and end

        #find statisfied with no window
        total = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total += customers[i]

        #l is start of window
        for i in range(minutes):
            if grumpy[i] == 1:
                total += customers[i]

        maxSat = total

        l, r = 0, minutes-1
        while r < len(customers)-1:

            # subtract left
            if grumpy[l] == 1:
                total -= customers[l]
            #l+=1, r+=1
            l+=1
            r+=1

            #summ += grumpy[i] * customers[i]
            if grumpy[r] == 1:
                total += customers[r]

            # max it 
            print(total)
            maxSat = max(maxSat, total)

        return maxSat




