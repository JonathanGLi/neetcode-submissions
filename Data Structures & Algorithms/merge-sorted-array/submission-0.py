class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        f1, f2, i = m-1, n-1, m+n-1

        print(f1, f2, i )

        while f1 >= 0 and f2 >=0:
            if nums1[f1] >= nums2[f2]:
                nums1[i] = nums1[f1]
                nums1[f1] = 0
                f1 -= 1
            elif nums1[f1] < nums2[f2]:
                nums1[i] = nums2[f2]
                nums2[f2] = 0
                f2 -= 1
            i -= 1

            print("nums1", nums1)
            print("nums2", nums2)

        for i in range(f2, -1, -1):
            nums1[i] = nums2[i]

        return nums1