class Solution(object):
    def spiralOrder(self, matrix):
        row = len(matrix)-1
        column = len(matrix[0])-1
        startCol = 0
        startRow = 0
        output = []
        while startRow <= row and startCol <= column:
            for c in range(startCol, column+1):
                output.append(matrix[startRow][c])
            startRow += 1

            for r in range(startRow, row+1):
                output.append(matrix[r][column])
            column -= 1

            if startRow <= row and startCol <= column:
                for c in range(column, startCol-1, -1):
                    output.append(matrix[row][c])
                row -= 1

            if startRow <= row and startCol <= column:
                for r in range(row, startRow-1, -1):
                    output.append(matrix[r][startCol])
                startCol += 1
        return output
