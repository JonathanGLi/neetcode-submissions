class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        D = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            D[n]+=1
        for n, c in D.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            while len(freq[i]) != 0:
                res.append(freq[i].pop())
                if len(res) == k:
                    return res