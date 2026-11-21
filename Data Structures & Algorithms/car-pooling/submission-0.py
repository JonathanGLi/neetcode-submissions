class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        

        map = defaultdict(int)


        for (numPass, fr, to) in trips:
            for i in range(fr, to):
                map[i] += numPass
                if map[i] > capacity:
                    return False


        return True
            