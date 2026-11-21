class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        


        l = 0
        res = 0

        #holds mins
        inc = deque()

        #hold maxes
        dec = deque()

        for r in range(len(nums)):

            while inc and inc[-1] > nums[r]:
                inc.pop()
            inc.append(nums[r])

            while dec and dec[-1] < nums[r]:
                dec.pop()
            dec.append(nums[r])

            while inc and dec and dec[0] - inc[0] > limit:
                if inc[0] == nums[l]:
                    inc.popleft()
                if dec[0] == nums[l]:
                    dec.popleft()
                l += 1

            res = max(res, r - l + 1)

        return res
