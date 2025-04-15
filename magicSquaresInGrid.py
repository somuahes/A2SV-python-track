class Solution(object):
    def numMagicSquaresInside(self, grid):
        def isMagic(i, j):
            nums = []
            for x in range(i, i+3):
                for y in range(j, j+3):
                    nums.append(grid[x][y])
            if sorted(nums) != list(range(1, 10)):
                return False
            return (
                sum(grid[i][j:j+3]) == 15 and
                sum(grid[i+1][j:j+3]) == 15 and
                sum(grid[i+2][j:j+3]) == 15 and
                grid[i][j]+grid[i+1][j]+grid[i+2][j] == 15 and
                grid[i][j+1]+grid[i+1][j+1] + grid[i+2][j+1] == 15 and
                grid[i][j+2]+grid[i+1][j+2] + grid[i+2][j+2] == 15 and
                grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2] == 15 and
                grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j] == 15)
        count = 0
        row = len(grid)
        column = len(grid[0])
        for i in range(row-2):
            for j in range(column-2):
                if isMagic(i, j):
                    count += 1
        return count
