class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        # First pass: mark all zeroes with 'v' in their row and column
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    # mark row
                    for col in range(cols):
                        if matrix[i][col] != 0:
                            matrix[i][col] = 'v'
                    # mark column
                    for row in range(rows):
                        if matrix[row][j] != 0:
                            matrix[row][j] = 'v'

        # Second pass: set 'v' to 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 'v':
                    matrix[i][j] = 0
        return matrix
