class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        

        mp = defaultdict(int)
        res = 0
        cursum = 0
        mp[0] = 1

        for n in nums:
            cursum += n

            diff = cursum - k

            if diff in mp:
                res += mp[diff]

            mp[cursum] += 1       

        return res 