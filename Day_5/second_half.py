import sys
sys.path.append('..')
from helper import get_lines, time_func

def split_data(lines):
    split_index = lines.index('\n')

    return (lines[0 : split_index], lines[split_index + 1 : ])

def format_stacks(lines):
    data, _ = split_data(lines)
    last_index = len(data) - 1
    number_indices = []
    stacks = []


    for index, value in enumerate(data[last_index]):
        if value != ' ' and value != '\n':
            number_indices.append(index)

    for index in number_indices:
        stack = []
        for item in data[0 : last_index]:
            data_point = item[index]
            if data_point != ' ':
                stack.insert(0, data_point)
        else:
            stacks.append(stack)

    return stacks

def format_instructions(lines):
    _, data = split_data(lines)
    NUM_INDEX = 1
    START_STACK_INDEX = 3
    DESTINATION_STACK_INDEX = 5
    instructions = []

    for line in data:
        new_line = line.replace('\n', '')
        new_line = new_line.split(' ')
        instructions.append((new_line[NUM_INDEX], 
                             new_line[START_STACK_INDEX], 
                             new_line[DESTINATION_STACK_INDEX]))

    return instructions

def work_data(lines):
    stacks = format_stacks(lines)
    instructions = format_instructions(lines)
    return (stacks, instructions)

def perform_instructions(stacks, instructions):
    new_stacks = stacks
    for num, start, des in instructions:
        num = int(num)
        start = int(start) - 1
        des = int(des) - 1
        num = (len(new_stacks[start]) - num)
        crates = new_stacks[start][num : ]
        new_stacks[des].extend(crates)
        new_stacks[start] = new_stacks[start][: num]


    return new_stacks


def read_top(stacks):
    running_string = ''
    for stack in stacks:
        top_element = stack.pop()
        running_string += top_element

    return running_string

def process():
    lines = get_lines()
    stacks, instructions = work_data(lines)
    new_stacks = perform_instructions(stacks, instructions)
    top_string = read_top(new_stacks)
    return top_string

if __name__ == '__main__':
    time_func(process)