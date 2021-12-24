from instruction import Instruction
from collections import defaultdict

instructions = []
x_limit = range(-50, 51)
y_limit = range(-50, 51)
z_limit = range(-50, 51)

with open ("C:\\Users\\ztang\\Desktop\\AdventCode2021\\Day22\\Day22Input.txt") as f:
    input = [x.strip().split(" ") for x in f.readlines()]
    input_switches = [1 if x[0] == "on" else 0 for x in input]
    coordinate_ranges = [x[1].split(",") for x in input ]

# print(coordinate_ranges)

for (switch, coordinate_range) in zip(input_switches, coordinate_ranges):
    instruction = Instruction()
    instruction.switch = switch
    for axis in coordinate_range:
        axis_range = range(int(axis[2:].split("..")[0]), int(axis.split("..")[1]) + 1)
        if axis[0] == "x":
            instruction.x_range = axis_range
        elif axis[0] == "y":
            instruction.y_range = axis_range
        elif axis[0] == "z":
            instruction.z_range = axis_range
    
    instructions.append(instruction)

cube_rec = defaultdict(lambda: False)

for instruction in instructions:
    for x in list(set(x_limit) & set(instruction.x_range)):
        for y in list(set(y_limit) & set(instruction.y_range)):
            for z in list(set(z_limit) & set(instruction.z_range)):
                cube_rec[(x, y, z)] = instruction.switch

result = 0

for x in cube_rec.values():
    if x:
        result += 1

print(result)


