import sys
sys.path.append('..')
from helper import get_stripped_lines, time_func
import heapq
import string

def parse_input(lines):
    graph = {}
    width, height = len(lines[0]), len(lines)
    start = goal = None
    elevation = dict(zip(string.ascii_lowercase, range(26)))
    elevation.update({'S': elevation['a'], 'E': elevation['z']})
    for y in range(height):
        for x in range(width):
            graph[(x, y)] = []
            cell = lines[y][x]
            if cell == 'S':
                start = (x, y)
                continue
            if cell == 'E':
                goal = (x, y)
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= nx < width and 0 <= ny < height:
                    if elevation[lines[ny][nx]] - elevation[cell] >= -1:
                        graph[(x, y)].append((nx, ny))
    return lines, graph, start, goal

def find_path(graph, goal):
    q = [(0, goal)]
    path_length = {goal: 0}
    while q:
        cost, current = heapq.heappop(q)
        for point in graph[current]:
            if point not in path_length or cost + 1 < path_length[point]:
                path_length[point] = cost + 1
                heapq.heappush(q, (cost + 1, point))
    return path_length

def process():
    lines = get_stripped_lines()
    grid, graph, start, goal = parse_input(lines)
    path_lengths = find_path(graph, goal)
    min_length = min(l for (x, y), l in path_lengths.items() if grid[y][x] in 'aS')
    return min_length

if __name__ == '__main__':
    time_func(process)
    