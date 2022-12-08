import sys
sys.path.append('..')
from helper import get_lines, time_func
from pathlib import Path

MAX_DISK_SPACE = 70000000
REQUIRED_DISK_SPACE = 30000000

def get_dir_tree(commands: list[str]) -> dict:
    level = Path('')
    dir_tree = {}
    for entry in commands:
        entry = entry.strip()
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
    
    total_space_used = dir_sizes[Path("/")]
    initial_free_space = MAX_DISK_SPACE - total_space_used
    clearable_space = REQUIRED_DISK_SPACE - initial_free_space

    min_removable_dir = (MAX_DISK_SPACE, Path('Random/Path'))

    for dir in dir_sizes:
        if dir_sizes[dir] >= clearable_space:
            if dir_sizes[dir] < min_removable_dir[0]:
                min_removable_dir = (dir_sizes[dir], dir)
    
    return min_removable_dir[0]

if __name__ == '__main__':
    time_func(process)
    