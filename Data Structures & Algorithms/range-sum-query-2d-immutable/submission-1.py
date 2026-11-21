class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.sumMatrix = [[0 for i in range(len(matrix[0]))]for j in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.sumMatrix[r][c] = matrix[r][c]
                if c > 0:
                    self.sumMatrix[r][c] += self.sumMatrix[r][c-1]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r > 0:
                    self.sumMatrix[r][c] += self.sumMatrix[r-1][c]

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        print(self.sumMatrix)
        full = self.sumMatrix[row2][col2]
        left, top, topleft = 0, 0, 0
        if col1 > 0:
            left = self.sumMatrix[row2][col1-1]
        if row1 > 0:
            top = self.sumMatrix[row1-1][col2]
        if col1 > 0 and row1 > 0:
            topleft = self.sumMatrix[row1-1][col1-1]

        return full + topleft - top - left

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)