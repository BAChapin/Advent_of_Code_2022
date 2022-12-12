import sys
sys.path.append('..')
from helper import get_stripped_lines, time_func
from monkeybus import Monkey

NUM_ROUNDS = 10_000

def get_data(input):
    running_data = []

    for index in range(0, len(input) + 1, 7):
        running_data.append(input[index : index + 6])

    return running_data

def run(monkeys, rounds):
    new_monkeys = monkeys

    for round in range(0, rounds):
        for index in range(0, len(new_monkeys)):
            current_monkey = new_monkeys[index]
            new_list = current_monkey.turn(new_monkeys, True)
            new_list[index] = current_monkey
    
    return new_monkeys

def process():
    lines = get_stripped_lines()
    data = get_data(lines)
    monkeys = list(map(Monkey, data))
    new_monkeys = run(monkeys, NUM_ROUNDS)
    values = list(monkey.items_inspected for monkey in new_monkeys)
    values.sort(reverse=True)

    return values[0] * values [1]

if __name__ == '__main__':
    time_func(process)
