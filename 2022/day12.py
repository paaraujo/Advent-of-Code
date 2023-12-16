import heapq
import numpy as np

from collections import deque
from tqdm import tqdm


def bfs(graph, start, end):
    queue = deque([(start, [start])])  # Queue contains tuples of (current_node, path_so_far)

    while queue:
        current_node, path = queue.popleft()

        for neighbor in graph[current_node].keys():
            if neighbor == end:
                return path + [neighbor], len(path + [neighbor]) -1  # Found the shortest path

            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))

    return None  # No path found


def dijkstra(graph, start, end):
    # Initialize distances, predecessors, and priority queue
    distances = {node: float('infinity') for node in graph}
    predecessors = {node: None for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        # Get the node with the smallest tentative distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # Check if the current distance is already greater than the known distance
        if current_distance > distances[current_node]:
            continue

        # Update distances to neighbors and predecessors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruct the shortest path
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = predecessors[current]

    return path, distances[end]


def check_condition(a,b):
    return (b - a) <= 1


# Building the graph
with open('inputs/day12.txt') as f:
    levels = f.readlines()
    levels = [list(level.strip()) for level in levels]
    levels = [list(map(ord,level)) for level in levels]

start_ASCii = 83
end_ASCii = 69

grid = np.array(levels)
max_i = grid.shape[0]
max_j = grid.shape[1]

start_index = np.argwhere(grid == start_ASCii)
row, col = start_index[0]
start_node = f'{row},{col}'
grid[row,col] = ord('a')

end_index = np.argwhere(grid == end_ASCii)
row, col = end_index[0]
end_node = f'{row},{col}'
grid[row,col] = ord('z')

graph = {}

for i in range(max_i):
    for j in range(max_j):
        # Building the nodes
        from_node = f'{i},{j}'
        graph[from_node] = {}
        if i-1 >= 0:
            if check_condition(grid[i,j],grid[i-1,j]):
                to_node = f'{i-1},{j}'
                temp_dict = graph[from_node]
                temp_dict[to_node] = 1
        if i+1 < max_i:
            if check_condition(grid[i,j],grid[i+1,j]):
                to_node = f'{i+1},{j}'
                temp_dict = graph[from_node]
                temp_dict[to_node] = 1
        if j-1 >= 0:
            if check_condition(grid[i,j],grid[i,j-1]):
                to_node = f'{i},{j-1}'        
                temp_dict = graph[from_node]
                temp_dict[to_node] = 1
        if j+1 < max_j:
            if check_condition(grid[i,j],grid[i,j+1]):
                to_node = f'{i},{j+1}'        
                temp_dict = graph[from_node]
                temp_dict[to_node] = 1


def part1():
    global graph, start_node, end_node
    path, size = dijkstra(graph=graph, start=start_node, end=end_node)
    # path, size = bfs(graph=graph, start=start_node, end=end_node)
    return size


all_start_indexes = np.argwhere(grid == ord('a'))

def part2():
    global graph, all_start_indexes, end_node
    steps = []
    with tqdm(total=len(all_start_indexes)) as pbar:
        for i,j in all_start_indexes:
            start_node = f'{i},{j}'
            _, size = dijkstra(graph=graph, start=start_node, end=end_node)
            steps.append([start_node, size])
            pbar.update(1)
    steps = sorted(steps, key=lambda x: x[1])
    return steps[0]

print(part1())
print(part2())