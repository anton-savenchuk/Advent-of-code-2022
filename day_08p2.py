grid = []

with open("input/day_08.txt", "r", encoding="utf-8") as file:
    grid.extend([int(i) for i in row.strip()] for row in file)


def get_column(line_id: int, column_id: int, len: int) -> int:
    top_column, down_column = [], []
    for i in range(len):
        if i < line_id:
            top_column.append(grid[i][column_id])
        elif i > line_id:
            down_column.append(grid[i][column_id])

    top_score = 0
    for i in top_column[::-1]:
        top_score += 1
        if i >= grid[line_id][column_id]:
            break

    down_score = 0
    for i in down_column:
        down_score += 1
        if i >= grid[line_id][column_id]:
            break

    return top_score * down_score


def get_line(line_id: int, column_id: int, len: int) -> int:
    left_line, right_line = [], []
    for j in range(len):
        if j < column_id:
            left_line.append(grid[line_id][j])
        elif j > column_id:
            right_line.append(grid[line_id][j])

    left_score = 0
    for i in left_line[::-1]:
        left_score += 1
        if i >= grid[line_id][column_id]:
            break

    right_score = 0
    for i in right_line:
        right_score += 1
        if i >= grid[line_id][column_id]:
            break

    return left_score * right_score


def get_score(index: tuple, len: int) -> int:
    line_id, column_id = index

    line_score = get_line(line_id, column_id, len)
    column_score = get_column(line_id, column_id, len)

    return line_score * column_score


len_grid = len(grid)
visible_grid = [[0] * len_grid for _ in range(len_grid)]

for i in range(1, len_grid - 1):
    for j in range(1, len_grid - 1):
        visible_grid[i][j] = get_score((i, j), len_grid)

highest_scenic_score = 0
for row in visible_grid:
    _max_row = max(row)

    if _max_row > highest_scenic_score:
        highest_scenic_score = _max_row

print(highest_scenic_score)
