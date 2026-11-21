class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        res = []
        m = defaultdict(int)

        for n in nums:
            m[n] += 1

            if m[n] > 2:
                m2 = defaultdict(int)

                for k in m:
                    if m[k] > 1:
                        m2[k] = m[k]-1

                m2 = m

        for k, v in m.items():
            if nums.count(k) > len(nums)//3:
                res.append(k)

        return res