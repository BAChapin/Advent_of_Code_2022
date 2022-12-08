import sys
sys.path.append('..')
from helper import get_lines, time_func
from pathlib import Path

def get_dir_tree(commands: list[str]) -> dict:
    level = Path('')
    dir_tree = {}
    for entry in commands:
        if '$ cd' in entry:
            if '..' in entry:
                level = level.parent
            else:
                direc_name = entry[5:]
                level = level / direc_name
                if level not in dir_tree:
                    dir_tree[level] = []
        elif 'dir' in entry:
            _, direc_name = entry.split(' ')
            dir_tree[level].append(level / direc_name)
        elif entry[0].isnumeric():
            file_size, file_name = entry.split(' ')
            dir_tree[level].append((file_name, int(file_size)))
    return dir_tree

def total_dir_size(dir_path: Path, dir_tree: dict) -> int:
    total_size = 0
    for object in dir_tree[dir_path]:
        if isinstance(object, tuple):
            total_size += object[1]
        elif isinstance(object, Path):
            total_size += total_dir_size(object, dir_tree)
    return total_size

def get_dir_sizes(dir_tree: dict) -> dict:
    return {dir: total_dir_size(dir, dir_tree) for dir in dir_tree}

def process():
    lines = get_lines()
    dir_tree = get_dir_tree(lines)
    dir_sizes = get_dir_sizes(dir_tree)

    return sum(dir_size for dir_size in dir_sizes.values() if dir_size < 100000)

if __name__ == '__main__':
    time_func(process)
