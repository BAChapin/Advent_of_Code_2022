import sys
sys.path.append('..')
from helper import get_stripped_lines, time_func

def get_instructions(lines):
    def convert(line):
        line = line.split()
        return (line[0], int(line[1]))
    
    return list(map(convert, lines))

def move_tail(tail, head):
    head_row, head_column = head
    row, column = tail

    diff_row, diff_column = (head_row - row, head_column - column)

    if abs(diff_row) <= 1 and abs(diff_column) <= 1:
        return tail

    if abs(diff_row) == 0 and abs(diff_column) > 1:
        return (row, int(column + (diff_column / 2)))
    elif abs(diff_row) == 1 and abs(diff_column) > 1:
        return (row + int((1 / diff_row)), column + int((diff_column / 2)))

    if abs(diff_column) == 0 and abs(diff_row) > 1:
        return (row + int((diff_row / 2)), column)
    elif abs(diff_column) == 1 and abs(diff_row) > 1:
        return (row + int((diff_row / 2)), column + int((1 / diff_column)))

        
    return tail

def run_instructions(instructions):
    head = (0, 0)
    tail = (0, 0)
    visited_positions = set()

    for dir, dis in instructions:
        for _ in range(0, dis):
            if dir == 'R':
                head = (head[0], head[1] + 1)
            elif dir == 'L':
                head = (head[0], head[1] - 1)
            elif dir == 'U':
                head = (head[0] + 1, head[1])
            elif dir == 'D':
                head = (head[0] - 1, head[1])

            tail = move_tail(tail, head)
            visited_positions.add(tail)

    return visited_positions

def process():
    lines = get_stripped_lines()
    instructions = get_instructions(lines)
    visited_pos = run_instructions(instructions)
    return len(visited_pos)

if __name__ == '__main__':
    time_func(process)