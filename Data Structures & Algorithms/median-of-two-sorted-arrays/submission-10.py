# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
#         A = nums1
#         B = nums2

#         #len A is shorted then B
#         if len(A) > len(B):
#             A, B = B, A

#         l = 0
#         r = len(A) - 1

#         half = (len(A) + len(B)) // 2

#         #use binary search to find the m index of A that corresonds to 
#         # a partition of the first hald elemnts in A+B
#         #then find median
#         while(True):
#             m_a = (l + r)//2

#             m_b = half - m_a - 2

#             # print(m_a, m_b)

#             a_1 = A[m_a] if m_a >=0 else float('-inf')
#             a_2 = A[m_a+1] if m_a < len(A) -1 else float('inf')

#             b_1 = B[m_b] if m_b >=0 else float('-inf')
#             b_2 = B[m_b+1] if m_b < len(B) -1 else float('inf')

#             # print(a_1, a_2, b_1, b_2)
#             #if correct partition
#             if a_1 < b_2 and b_1 < a_2:
#                 if ((len(A) + len(B)) % 2 == 1):
#                     return min(a_2, b_2)
#                 else:
                    
#                     return ((max(a_1, b_1) + min(a_2, b_2))/2)

#             elif a_1 >= b_2:
#                 r = m_a - 1
#             else:
#                 l = m_a+1




class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
