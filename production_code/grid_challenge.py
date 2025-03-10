def grid_challenge(grid):
    sorted_rows = [sorted(row) for row in grid]
    for col in range(len(sorted_rows[0])):
        for row in range(len(sorted_rows) - 1):
            if sorted_rows[row][col] > sorted_rows[row + 1][col]:
                return "NO"
    return "YES"