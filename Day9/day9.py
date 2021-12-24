def get_basin_size(row_i, col_i, neighbor_value):
    value = input[row_i][col_i]
    if value >= 9 or value <= neighbor_value:
        return 0
    elif (row_i, col_i) in rec:
        return 0
    else:
        rec.add((row_i, col_i))
        return 1 + get_basin_size(row_i + 1, col_i, value) + get_basin_size(row_i - 1, col_i, value) + get_basin_size(row_i, col_i + 1, value) + get_basin_size(row_i, col_i - 1, value)
        


def part2(low_points: list, input: list):
    basin_sizes = []
    for low_point in low_points:
        row_i = low_point[0]
        col_i = low_point[1]
        value = input[row_i][col_i]
        if (row_i, col_i) not in rec:
            rec.add((row_i, col_i))
            basin_sizes.append(1 + get_basin_size(row_i + 1, col_i, value) + get_basin_size(row_i - 1, col_i, value) +
                           get_basin_size(row_i, col_i + 1, value) + get_basin_size(row_i, col_i - 1, value))

    basin_sizes.sort()
    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


input = []
rec = set()
with open("C:\\Users\\ztang\\Desktop\\AdventCode2021\\Day9\\Day9Input.txt") as f:
    input = [[int(x) for x in list(line.strip())] for line in f.readlines()]

row_number = len(input)
col_number = len(input[0])

input.insert(0, [10] * col_number)
input.insert(row_number + 1, [10] * col_number)

for row in input:
    row.insert(0, 10)
    row.insert(col_number + 1, 10)

# print(input)
result = 0
low_points = []

for row_i in range(1, row_number+1):
    for col_i in range(1, col_number+1):
        value = input[row_i][col_i]

        if value < min(input[row_i + 1][col_i], input[row_i - 1][col_i], input[row_i][col_i + 1], input[row_i][col_i - 1]):
            result += (value + 1)
            low_points.append((row_i, col_i))

print(result)
print(part2(low_points, input))
