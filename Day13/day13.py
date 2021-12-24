input_dots = []
input_fold = []
transparent = set()

with open ("C:\\Users\\ztang\\Desktop\\AdventCode2021\\Day13\\Day13Input.txt") as f:
    input = f.read().split("\n\n")
    input_dots = [[int(point) for point in x.split(",")] for x in input[0].split("\n")]
    input_fold = [x[11:].split("=") for x in input[1].split("\n")]

for point in input_dots:
    transparent.add((point[0], point[1]))

# print(transparent)

for instruction in input_fold:
    if instruction[0] == "x":
        horizontal_fold = True
    else:
        horizontal_fold = False
    line_number = int(instruction[1])

    dots_to_add = []
    dots_to_remove = []
    for point in transparent:
        (x,y) = point
        if horizontal_fold and x >= line_number:
            dots_to_remove.append(point)
            dots_to_add.append((line_number + (line_number -x), y))
        if horizontal_fold and x == line_number:
            dots_to_remove.append(point)
        if not horizontal_fold and y >= line_number:
            dots_to_remove.append(point)
            dots_to_add.append((x, line_number - (y - line_number)))
        if not horizontal_fold and y == line_number:
            dots_to_remove.append(point)
    
    for dots in dots_to_remove:
        transparent.remove(dots)
    
    for dots in dots_to_add:
        transparent.add(dots)
    
    print(len(transparent))
    
# print(transparent)
print(len(transparent))
#print(transparent)
for y in range(max(y for _,y in transparent)+1):
    for x in range(max(x for x, _ in transparent)+1):
        print('.#'[(x,y) in transparent], end='')
    print()




