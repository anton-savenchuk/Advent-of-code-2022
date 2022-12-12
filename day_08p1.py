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

    return (grid[line_id][column_id] > max(top_column)) + (
        grid[line_id][column_id] > max(down_column)
    )


def get_line(line_id: int, column_id: int, len: int) -> int:
    left_line, right_line = [], []
    for j in range(len):
        if j < column_id:
            left_line.append(grid[line_id][j])
        elif j > column_id:
            right_line.append(grid[line_id][j])

    return (grid[line_id][column_id] > max(left_line)) + (
        grid[line_id][column_id] > max(right_line)
    )


def get_visible(index: tuple, len: int) -> bool:
    line_id, column_id = index

    line = get_line(line_id, column_id, len)
    column = get_column(line_id, column_id, len)

    return (line + column) >= 1


len_grid = len(grid)
visible_grid = [[1] * len_grid for _ in range(len_grid)]

for i in range(1, len_grid - 1):
    for j in range(1, len_grid - 1):
        visible_grid[i][j] = get_visible((i, j), len_grid)

visible_trees_counter = sum(sum(row) for row in visible_grid)

print(visible_trees_counter)
