class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        

        x, y, z = 0, 0, 0
        for a, b, c in triplets:



            if a<= target[0] and b<= target[1] and c<= target[2]:
                x = max(a, x)
                y = max(b, y)
                z = max(c, z)

        return [x, y, z] == target
                