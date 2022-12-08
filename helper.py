from time import time

def get_lines():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    return lines

def get_stripped_lines():
    with open('input.txt', 'r') as puzzle_input:
        return [line.strip() for line in puzzle_input.readlines()]

def time_func(func):
    answer = None
    start_time = time()
    for i in range(0, 10):
        answer = func()
    end_time = time()
    elapsed_time = end_time - start_time
    average = elapsed_time / 10
    print('Answer:', answer)
    print('Average Elapsed Time:', average)