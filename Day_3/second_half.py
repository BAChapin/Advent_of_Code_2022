import sys
sys.path.append('..')
from helper import get_lines, time_func

def create_groups(lines):
    length = len(lines) + 1
    step = 3
    previous_index = 0
    running_list = []
    for i in range(3, length, step):
        sub_list = lines[previous_index:i]
        sub_list.sort(key = len)
        previous_index = i
        running_list.append(sub_list)
    else:
        return running_list

def common_element(lines):
    for i in lines[0]:
        if i in lines[1] and i in lines[2]:
            return i

def score(element):
    score_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = score_list.index(element) + 1
    return index

def process():
    lines = get_lines()
    grouped_elves = create_groups(lines)
    common_elements = list(map(common_element, grouped_elves))
    scored_elements = list(map(score, common_elements))
    total_score = sum(scored_elements)
    return total_score


if __name__ == '__main__':
    time_func(process)