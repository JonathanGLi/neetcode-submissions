class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        def to2d(m, n, i):
            r = i // n
            c = i % n
            return r, c

        def to1d(m, n, r, c):
            return n * r + c

        l_r = 0
        l_c = 0

        r_r = m-1
        r_c = n-1

        while(to1d(m, n, l_r, l_c) <= to1d(m, n, r_r, r_c)):

            midd = int((to1d(m, n, l_r, l_c) + to1d(m, n, r_r, r_c)) // 2)
            mid_r, mid_c = to2d(m, n, midd)

            if (matrix[mid_r][mid_c] == target):
                return True

            elif (matrix[mid_r][mid_c] < target):
                l_r, l_c = to2d(m, n, midd+1)
            elif (matrix[mid_r][mid_c] > target):
                r_r, r_c = to2d(m, n, midd-1)

        return False
        