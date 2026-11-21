
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # map each elem to count
        #X 2, Y 2
        #(cout, Letter) in queue of n elems
        # A A A B B B C 2
        # A4 B4, 3

        # want to keep n largest letter coutns in Queue and rest in maxheap 2


        # A3 B3 - C
        #B3, A2 - C
        #A2, B2 - C
        #B2, A1 - C
        #A1 B1, C
        #B1, C
        #B1, C

        #A3 b3, C3
        #B3 c3, A2
        #C3 B2, A2
        #B2 C2, A2
        #C2 A2, B1
        #A2 C1, B1
        #C1 A1, B1
        #C B A

        #A B C B C A C B A

        # n log n, n



        q = deque()
        for i in range(n+1):
            q.append((0, 0))

        count = defaultdict(int)
        for c in tasks:
            count[c] += 1

        heap = [(0, 0)]
        for key, val in count.items():
            heapq.heappush(heap, (-val, key))

        print(q)
        print(heap)
        res = 0

        load = n+1
        
        while True:
            

            c1, l1 = q.popleft()

            c, l = heapq.heappop(heap)
            c, l = -c, l
            print(q)
            print(heap)
            print(c1, l1)
            print(c, l)


            if (c) == (0) and (c1) == (0):
                nonZero = True
                for (a, b) in q:
                    if a > 0:
                        nonZero = False
                if nonZero:
                    break
                q.append((0, 0))
                heapq.heappush(heap, (0, 0))
            elif c > c1:
                if c1 >0:
                    heapq.heappush(heap, (-c1, l1))
                q.append((c-1, l))
                print('A')
                load = n+1
            elif c1 >= c:
                c1 -= 1
                if c1 <= 0:
                    q.append((0, 0))
                else:
                    q.append((c1, l1))
                if c > 0 or c == 0:
                    heapq.heappush(heap, (-c, l))
                print('B')


            res += 1
            
        return res
                









