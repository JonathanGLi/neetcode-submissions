class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # create dictionary number:count O(n)
        D = {}

        for n in nums:
            D[n] = D.get(n, 0)+1

        #array, index is count, value is number n(log n)
        arr = []
        for num, count in D.items():
            arr.append([count, num])
        arr.sort()


        # return highest k values of array
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
