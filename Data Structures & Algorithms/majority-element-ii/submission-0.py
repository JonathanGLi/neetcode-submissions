class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        

        #n, n

        res = set()

        bound = len(nums)//3

        m = defaultdict(int)

        for n in nums:
            m[n] += 1

            if m[n] > bound:
                res.add(n)

        return list(res)
