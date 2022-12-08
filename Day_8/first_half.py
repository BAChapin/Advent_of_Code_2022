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
    check = True
    
    # Check Left
    for l in range(0, column):
        if tree_height <= grid[row][l]:
            check = False
            break
    else:
        if check:
            return True

    # Check Right
    check = True
    for r in range(column + 1, column_num):
        if tree_height <= grid[row][r]:
            check = False
            break
    else:
        if check:
            return True

    # Check Up
    check = True
    for u in range(0, row):
        if tree_height <= grid[u][column]:
            check = False
            break
    else:
        if check:
            return True

    # Check Down
    check = True
    for d in range(row + 1, row_num):
        if tree_height <= grid[d][column]:
            check = False
            break
    else:
        if check:
            return True

    return False

def inner_visible_trees(grid: list[list[int]]):
    visible_trees = []
    row_num = len(grid)
    column_num = len(grid[0])

    for row_id in range(1, row_num - 1):
        for column_id in range(1, column_num - 1):
            if check_visibility((row_id, column_id), grid):
                visible_trees.append((row_id, column_id))

    return visible_trees

def perimeter_trees(grid):
    height = len(grid) - 1
    width = len(grid[0]) - 1
    return (height + width) * 2

def process():
    lines = get_stripped_lines()
    grid = get_grid(lines)
    visible_trees = inner_visible_trees(grid)
    perimeter = perimeter_trees(grid)
    return len(visible_trees) + perimeter


if __name__ == '__main__':
    time_func(process)