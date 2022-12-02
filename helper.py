from time import time

def get_lines():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    return lines

def time_func(func):
    answer = None
    start_time = time()
    for i in range(0, 10):
        answer = func()
    end_time = time()
    elapsed_time = end_time - start_time
    average = elapsed_time / 10
    return (average, answer)