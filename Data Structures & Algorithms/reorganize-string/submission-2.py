class Solution:
    def reorganizeString(self, s: str) -> str:

        count = Counter(s)

        heap = [(-count, char) for char, count in count.items()]
        heapq.heapify(heap)

        res = ""

        prev = None

        while heap or prev:
            if prev and not heap:
                return ""

            count, char = heapq.heappop(heap)
            count+= 1
            res += char

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if count < 0:
                prev = (count, char)

        return res












