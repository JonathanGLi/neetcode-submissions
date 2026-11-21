class Solution:
    def reorganizeString(self, s: str) -> str:
        #1158
        #n, n

        if len(s) == 0:
            return ""


        if len(s) == 1:
            return s


        m = defaultdict(int)

        for c in s:
            m[c] += 1

        if len(m) == 1:
            return ""

        print(m)

        #maxheap
        h = []
        heapq.heapify(h)

        for k, v in m.items():
            heapq.heappush(h, (-v, k))

        print(h)
        #take top off

        (count1, char1) = heapq.heappop(h)
        (count2, char2) = heapq.heappop(h)


        res = ""
        while True:
            res += str(char1)
            if count1+1 < 0:
                heapq.heappush(h, (count1+1, char1))
            count1, char1 = count2, char2
            if h:
                (count2, char2) = heapq.heappop(h)
            else:
                break

            print(h)

        res += str(char1)

        if count1 < -1:
            return ""


        return res












