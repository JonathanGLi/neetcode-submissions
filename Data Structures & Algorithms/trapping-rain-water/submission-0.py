class Solution:
    def trap(self, height: List[int]) -> int:
        

        l, r = 0, len(height)-1
        lMax, rMax = 0, 0
        lSum, rSum = 0, 0

        while l < r:
            print("l: " + str(l) + ", r: " + str(r))
            print("lSum: " + str(lSum) + ", rSum: " + str(rSum))

            if height[l] > lMax:
                lMax = height[l]
            else:
                lSum += (lMax - height[l])

            if height[r] > rMax:
                rMax = height[r]
            else:
                rSum += (rMax - height[r])

            if height[l] <= height[r]:
                l+=1
            else:
                r-=1

        return lSum + rSum