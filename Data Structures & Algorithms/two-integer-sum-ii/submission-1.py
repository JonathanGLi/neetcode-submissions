class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        D = {}

        for i, n in enumerate(numbers):
            c = target - n

            if c in D:
                return [D[c]+1, i+1]

            D[n] = i
