import sys
sys.path.append('..')
from helper import get_lines, time_func

def scan(line):
    data_length = len(line)

    for i in range(4, data_length - 1):
        substring = line[i - 4: i]
        all_unique = True
        for c in substring:
            if substring.count(c) > 1:
                all_unique = False
        else:
            if all_unique:
                return i

def process():
    lines = get_lines()
    index = scan(lines[0])
    return index

if __name__ == '__main__':
    time_func(process)