class Solution(object):
    def findDiagonalOrder(self, mat):
        row = len(mat)
        column = len(mat[0])
        output = []
        curRow = 0
        curCol = 0
        goingUp = True
        while len(output) != row*column:
            if goingUp:
                while curRow >= 0 and curCol < column:
                    output.append(mat[curRow][curCol])
                    curRow -= 1
                    curCol += 1
                if curCol == column:
                    curCol -= 1
                    curRow += 2
                else:
                    curRow += 1

                goingUp = False
            else:
                while curRow < row and curCol >= 0:
                    output.append(mat[curRow][curCol])
                    curRow += 1
                    curCol -= 1
                if curRow == row:
                    curCol += 2
                    curRow -= 1
                else:
                    curCol += 1
                goingUp = True
        return output
