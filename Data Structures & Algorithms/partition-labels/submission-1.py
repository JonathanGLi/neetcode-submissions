class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        

        # map each character to the last indx it is seen
        ends = {}

        for i, c in enumerate(s):
            ends[c] = i

        res = []
        size = 0
        #loop though s
        end = 0
        for i, c in enumerate(s):

            #we update the end of the current subseq at each character until we read the end
            end = max(end, ends[c])
            size += 1
            #then we reset the size and start a new subsequence(append to res)
            if end == i:
                res.append(size)
                size = 0


        return res

        #abcabc
        #a => 3
        #b => 4
        #c => 5

        # end = 4, size = 2
