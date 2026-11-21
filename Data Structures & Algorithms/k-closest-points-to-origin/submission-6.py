class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        


        def dist_fn(point):
            return point[0]**2 + point[1]**2

        return heapq.nsmallest(k, points, key = dist_fn)
