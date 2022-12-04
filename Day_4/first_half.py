import sys
sys.path.append('..')
from helper import get_lines, time_func

def get_pair(line):
    line = line.replace('\n', '')
    return tuple(line.split(','))

def get_ranges(pair):
    first, second = pair
    first_values = tuple(map(int, first.split('-')))
    second_values = tuple(map(int, second.split('-')))
    return (first_values, second_values)

def contains_range(pair):
    first, second = pair
    a, b = first
    c, d = second
    
    return a <= c <= d <= b or c <= a <= b <= d

def process():
    lines = get_lines()
    pairs = list(map(get_pair, lines))
    ranges = list(map(get_ranges, pairs))
    check = list(map(contains_range, ranges))
    return check.count(True)

if __name__ == '__main__':
    time_func(process)