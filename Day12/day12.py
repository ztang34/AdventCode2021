topo = {}
input = []
paths = []

def add_to_topo(point_1, point_2):
    if point_1 not in topo:
        topo[point_1] = [point_2]
    else:
        topo[point_1].append(point_2)

with open("C:\\Users\\ztang\\Desktop\\AdventCode2021\\Day12\\Day12Input.txt") as f:
    input = [line.strip().split("-") for line in f.readlines()]

for link in input:
    point_1 = link[0]
    point_2 = link[1]

    if point_1 == "start":
        add_to_topo(point_1, point_2)
    elif point_1 == "end":
        add_to_topo(point_2, point_1)
    elif point_2 == "start":
        add_to_topo(point_2, point_1)
    elif point_2 == "end":
        add_to_topo(point_1, point_2)
    else:
        add_to_topo(point_1, point_2)
        add_to_topo(point_2, point_1)

for node in topo["start"]:
    small_cave_set = set()
    if not node.isupper():
        small_cave_set.add(node)
    paths.append(([node], small_cave_set, False))

result = 0
while len(paths) != 0:
    entry = paths.pop(0)
    path = entry[0]
    small_cave_set = entry[1]
    singe_small_cave_visited_twice = entry[2]

    if path[-1] == "end":
        result += 1
    else: 
        for node in topo[path[-1]]:
            small_cave_set_update = small_cave_set.copy()
            if not node.isupper() and node not in small_cave_set:
                small_cave_set_update.add(node)
                paths.append((path + [node], small_cave_set_update, singe_small_cave_visited_twice))
            elif not node.isupper() and node in small_cave_set and not singe_small_cave_visited_twice:
                paths.append((path + [node], small_cave_set_update, True))
            elif node.isupper():
                paths.append((path + [node], small_cave_set_update, singe_small_cave_visited_twice))
    


print(result)


