class Solution:
    def trap(self, height: List[int]) -> int:
        
        #left right points moving in

        #left max right max

        #shorter side moves
        #left sum right sum
        #add sum as it moves


        l = 0
        r = len(height)-1
        l_max = 0
        r_max = 0
        l_sum = 0
        r_sum = 0

        while (l < r) :


            r_max = max(r_max, height[r])
            l_max = max(l_max, height[l])

            l_sum += l_max - height[l]
            r_sum += r_max - height[r]
            


            if (height[l] > height[r]):
                r-=1
            else:
                l+=1

        return l_sum + r_sum


        #lmax  2
        #rmax  2
        #lsum  2
        #rsum  0
        #l  3
        #r  7