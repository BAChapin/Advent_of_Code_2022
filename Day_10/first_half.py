import sys
sys.path.append('..')
from helper import get_stripped_lines, time_func

def run(instructions):
    cycles = 0
    x = 1
    ops = []

    for instruction in instructions:
        if instruction == 'noop':
            cycles += 1
        else:
            cmd, val = instruction.split()
            cycles += 2
            x += int(val)
            ops.append((cycles, x))

    return ops

def find_x(cycle, ops):

    for index, item in enumerate(ops):
        cyc, val = item
        for_cyc, for_val = ops[index + 1]
        if cyc == cycle:
            _, past_val = ops[index - 1]
            return past_val

        if for_cyc > cycle and cyc < cycle:
            return val

def sum_x(cycles, ops):
    running_sum = 0

    for cycle in cycles:
        val = find_x(cycle, ops)
        running_sum += (cycle * val)

    return running_sum

def process():
    lines = get_stripped_lines()
    ops = run(lines)
    val_sum = sum_x([20, 60, 100, 140, 180, 220], ops)
    return val_sum

if __name__ == '__main__':
    time_func(process)
