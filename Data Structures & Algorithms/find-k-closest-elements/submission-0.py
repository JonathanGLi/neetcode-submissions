class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # 2, 4 , 5, 8
        # 2, 4
        # 4, 5
        # 5, 8

        #i = 0, j = k - 1


        for i in range(len(arr) - k):
            if abs(arr[i + k] - x) >= abs(arr[i] - x):
                return [arr[j] for j in range(i, i + k)]

        return [arr[j] for j in range(len(arr) - k, len(arr))]
