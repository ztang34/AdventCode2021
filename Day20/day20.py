import copy

algorithm = []
input_image = []
cycles = 50

def expand_image(input_image: list, padding):
    dimension = len(input_image)
    input_image.insert(0, [padding]  * dimension)
    input_image.append([padding] * dimension)

    for row in input_image:
        row.insert(0, padding)
        row.append(padding)
    
    return

def get_pixel_value(input_image, row_index, col_index, padding):
    dimension = len(input_image)

    if row_index < 0 or row_index >= dimension or col_index < 0 or col_index >= dimension:
        return padding
    else:
        return input_image[row_index][col_index]

with open ("C:\\Users\\ztang\\Desktop\\AdventCode2021\\Day20\\Day20Input.txt") as f:
    input = f.read().split("\n\n")
    algorithm = ["1" if x == "#" else "0" for x in input[0]]
    input_image = [["1" if x == "#" else "0" for x in line] for line in input[1].split("\n")]

    
for cycle in range(cycles):
    if cycle % 2 == 0:
        padding = "0"
    else:
        padding = "1"
    
    expand_image(input_image, padding)
    output_image = copy.deepcopy(input_image)

    for row_index in range(len(input_image)):
        for col_index in range(len(input_image)):
            algorithm_index_string = ""
            neighbors = [(row_index - 1, col_index -1), (row_index -1, col_index), (row_index -1, col_index + 1),
            (row_index, col_index -1), (row_index, col_index), (row_index, col_index + 1), (row_index + 1, col_index -1),
            (row_index + 1, col_index), (row_index + 1, col_index + 1)]

            for neighbor in neighbors:
                algorithm_index_string += get_pixel_value(input_image, neighbor[0], neighbor[1], padding)
            
            algorithm_index = int(algorithm_index_string, 2)
            output_image[row_index][col_index] = algorithm[algorithm_index]
    
    input_image = output_image

count = 0
for row in input_image:
    for val in row:
        if val == "1":
            count += 1

print(count)
           


