class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        

        ROWS = len(points)
        COLS = len(points[0])

        row = points[0]

        for i in range(1, ROWS):

            new_row = points[i].copy()

            left = [0] * COLS
            right = [0] * COLS

            left[0] = row[0]
            for j in range(1, COLS):
                left[j] = max(row[j], left[j-1] - 1)

            right[COLS-1] = row[COLS-1]
            for j in range(COLS-2, -1, -1):
                right[j] = max(row[j], right[j+1] - 1)

            for j in range(0, COLS):
                new_row[j] += max(left[j], right[j])

            row =new_row

        return max(row)
