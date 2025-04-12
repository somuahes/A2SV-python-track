n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
result = ""
for i in range(n):
    for j in range(m):
        letter = grid[i][j]
        countInRow = grid[i].count(letter)

        countInColumn = 0
        for y in range(n):
            if grid[y][j] == letter:
                countInColumn += 1
        if countInRow == 1 and countInColumn == 1:
            result += letter
print(result)
