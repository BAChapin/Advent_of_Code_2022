import sys
sys.path.append('..')
from helper import get_stripped_lines, time_func
import functools

def read_input(lines):
    inputs = []
    for line in lines:
        if not line:
            continue

        end, line = parse_list(line, 0)

        inputs.append(line)
    return inputs

def parse_list(line, index):
    output = []
    assert line[index] == '[', 'Something is fishy.'
    index += 1

    while index < len(line):
        if line[index] == '[':
            index, rec_list = parse_list(line, index)
            output.append(rec_list)
        elif line[index].isdigit():
            end = index
            while end < len(line) and line[end].isdigit():
                end += 1

            number = int(line[index:end])

            output.append(number)

            index = end
        elif line[index] == ',':
            index += 1

        elif line[index] == ']':
            break

        else:
            print(index, line[index])
            raise NotImplemented

    return index + 1, output

def list_comparison(lhs, rhs):
    for ele1, ele2 in zip(lhs, rhs):
        if isinstance(ele1, int) and isinstance(ele2, int):
            if ele1 < ele2:
                return -1
            elif ele1 > ele2:
                return 1

        elif isinstance(ele1, list) or isinstance(ele2, list):
            if isinstance(ele1, int):
                ele1 = [ele1]
            if isinstance(ele2, int):
                ele2 = [ele2]

            result = list_comparison(ele1, ele2)

            if result:
                return result

    if len(lhs) < len(rhs):
        return -1
    elif len(lhs) > len(rhs):
        return 1
    else:
        return 0

def custom_bisect(arr, target, comparator):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left)//2

        if comparator(arr[mid], target) == -1:
            left = mid + 1
        else:
            right = mid
    return right + 1

# use custom comp function for python sorting similar to
# https://stackoverflow.com/questions/32752739/how-does-the-functools-cmp-to-key-function-work
def process():
    lines = get_stripped_lines()
    inputs = read_input(lines)
    key = functools.cmp_to_key(list_comparison)
    inputs.sort(key=key)

    first = custom_bisect(inputs, [[2]], list_comparison)
    second = custom_bisect(inputs, [[6]], list_comparison) + 1
    return first * second

if __name__ == '__main__':
    time_func(process)