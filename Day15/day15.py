import sys
import heapq
from collections import defaultdict

input = []
prev_node = {}
visited_nodes = set()
min_distance = []

def get_neighbor(coordinates, length):
    neighbors = []

    (x,y) = coordinates
    if x -1 >=0:
        neighbors.append((x-1,y))
    if x + 1 < length:
        neighbors.append((x+1, y))
    if y -1 >= 0:
        neighbors.append((x, y-1))
    if y +1 < length:
        neighbors.append((x, y+1))
    
    return neighbors


with open("C:\\Users\\ztang\\Desktop\\AdventCode2021\\Day15\\Day15Input.txt") as f:
    input = [[int(n) for n in list(x.strip())] for x in f.readlines()]



# for part 2
n = 5
block_len = len(input)
for i in range(block_len * n):
    if i >= block_len:
        input.append([])
    for j in range(block_len * n ):
        if (i < block_len and j >=block_len) or i >=block_len:
            block_value = input[i % block_len][j % block_len]
            added_value = (i // block_len) + (j // block_len)
            total_value = block_value + added_value
            if total_value < 10:
                input[i].append((block_value + added_value) % 10)
            else:
                input[i].append((block_value + added_value) % 10 +1)

print(input)


#initialize distance 
distance = defaultdict(lambda: sys.maxsize)
distance[(0,0)] = 0

#initialize min_distance heap
heapq.heappush(min_distance, (0, (0,0)))

while min_distance:
    (current_value, current_node) = heapq.heappop(min_distance)

    if current_node in visited_nodes:
        continue
    else:
        visited_nodes.add(current_node)
        neighbors = get_neighbor(current_node, len(input))
        for neighbor in neighbors:
            (x, y) = neighbor
            temp_distance = distance[current_node] + input[x][y]
            if temp_distance < distance[neighbor]:
                distance[neighbor] = temp_distance
                heapq.heappush(min_distance, (temp_distance, neighbor))





print(distance[(len(input) -1, len(input) - 1)])
    
    


    


