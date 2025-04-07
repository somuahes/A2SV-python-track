class Solution(object):
    def transpose(self, matrix):
        rows = len(matrix)
        column = len(matrix[0])
        output = []
        for i in range(column):
            new_row = []
            for j in range(rows):
                new_row.append(matrix[j][i])
            output.append(new_row)
        return output
