import sys
sys.path.append('..')
from helper import get_lines, time_func
import functools

def chunk_data(lines):
    new_list = []
    temp_list = []
    for i in lines:
        if i == "\n":
            list_sum = sum(temp_list)
            new_list.append(list_sum)
            temp_list = []
        else:
            temp_list.append(int(i))
    else:
        return new_list

def process():
    lines = get_lines()
    chunked_data = chunk_data(lines)
    chunked_data.sort(reverse=True)
    top_3_sum = 0

    for i in range(0, 3):
        top_3_sum += chunked_data[i]
    else:
        print(top_3_sum)

if __name__ == "__main__":
    time_func(process)