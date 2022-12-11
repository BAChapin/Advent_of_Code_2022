import sys
sys.path.append('..')
from helper import get_stripped_lines, time_func

def run(instructions):
    cmd_index = 0
    running_cmd = None
    cmd_fin = False
    current_cycle = 1
    current_pos = 1
    draw_pos = 0
    current_line = ''
    screen = []

    while (cmd_index < len(instructions)):
        # Start of Cycle
        current_instruction = instructions[cmd_index]
        if running_cmd is None and current_instruction != 'noop':
            running_cmd = current_instruction
        elif running_cmd is not None:
            cmd_fin = True
        else:
            cmd_index += 1
        # During Cycle
        diff = current_pos - draw_pos
        if abs(diff) <= 1:
            current_line += '#'
        else:
            current_line += '.'
        # End of Cycle
        current_cycle += 1
        draw_pos += 1
        if cmd_fin is True:
            _, val = running_cmd.split()
            current_pos += int(val)
            running_cmd = None
            cmd_fin = False
            cmd_index += 1
        if len(current_line) == 40:
            draw_pos = 0
            screen.append(current_line)
            current_line = ''

    return screen

def process():
    lines = get_stripped_lines()
    screen = run(lines)
    
    return screen

if __name__ == '__main__':
    time_func(process)
