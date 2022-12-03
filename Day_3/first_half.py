import sys
sys.path.append('..')
from helper import get_lines, time_func

def split_items(line):
    length = len(line) if '\n' not in line else len(line) - 1
    half_length = int(length / 2)
    return (line[0:half_length], line[half_length:-1])

def common_element(line):
    first = line[0]
    second = line[1]
    for i in first:
        if i in second:
            return i

def score(element):
    score_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = score_list.index(element) + 1
    return index

def process():
    lines = get_lines()
    split_lines = list(map(split_items, lines))
    common_elements = list(map(common_element, split_lines))
    scored_elements = list(map(score, common_elements))
    total_score = sum(scored_elements)
    return total_score

if __name__ == '__main__':
    time_func(process)