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
    
    largest_calorie = functools.reduce(lambda a, b: a if a > b else b, chunked_data)
    print(largest_calorie)

if __name__ == "__main__":
    time_func(process)