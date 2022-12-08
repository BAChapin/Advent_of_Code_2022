import sys
sys.path.append('..')
from helper import get_stripped_lines, time_func

def get_grid(lines):
    grid = []
    current_row = []
    for line in lines:
        for i in line:
            current_row.append(int(i))
        else:
            grid.append(current_row)
            current_row = []
    return grid

def check_visibility(pos, grid: list[list[int]]) -> bool:
    row, column = pos
    tree_height = grid[row][column]
    row_num = len(grid)
    column_num = len(grid[0])
    right = 0
    left = 0
    up = 0
    down = 0
    
    # Check Left
    left_range = list(range(0, column))
    left_range.sort(reverse=True)
    for l in left_range:
        if tree_height <= grid[row][l]:
            left += 1
            break
        else:
            left += 1

    # Check Right
    for r in range(column + 1, column_num):
        if tree_height <= grid[row][r]:
            right += 1
            break
        else:
            right += 1

    # Check Up
    up_range = list(range(0, row))
    up_range.sort(reverse=True)
    for u in up_range:
        if tree_height <= grid[u][column]:
            up += 1
            break
        else:
            up += 1

    # Check Down
    for d in range(row + 1, row_num):
        if tree_height <= grid[d][column]:
            down += 1
            break
        else:
            down += 1

    return right * left * up * down

def inner_visible_trees(grid: list[list[int]]):
    tree_visibility = []
    row_num = len(grid)
    column_num = len(grid[0])

    for row_id in range(1, row_num - 1):
        for column_id in range(1, column_num - 1):
            tree_visibility.append(check_visibility((row_id, column_id), grid))

    return tree_visibility

def process():
    lines = get_stripped_lines()
    grid = get_grid(lines)
    tree_visibility = inner_visible_trees(grid)
    tree_visibility.sort(reverse=True)
    return tree_visibility[0]


if __name__ == '__main__':
    time_func(process)