def update_after_flash(input, row_i, col_i):
    input[row_i-1][col_i - 1] += 1 if input[row_i-1][col_i - 1]> 0 else 0
    input[row_i-1][col_i] += 1 if input[row_i-1][col_i]> 0 else 0
    input[row_i-1][col_i + 1] += 1 if input[row_i-1][col_i + 1]> 0 else 0
    input[row_i][col_i - 1] += 1 if input[row_i][col_i - 1]> 0 else 0
    input[row_i][col_i + 1] += 1 if input[row_i][col_i + 1]> 0 else 0
    input[row_i + 1][col_i - 1] += 1 if input[row_i + 1][col_i - 1]> 0 else 0
    input[row_i + 1][col_i] += 1 if input[row_i + 1][col_i]> 0 else 0
    input[row_i + 1][col_i + 1] += 1 if input[row_i + 1][col_i + 1]> 0 else 0


input = []
total_steps = 200
total_flashes = 0

with open("C:\\Users\\ztang\\Desktop\\AdventCode2021\\Day11\\Day11Input.txt") as f:
    input = [[int(x) for x in list(line.strip())] for line in f.readlines()]

# set up boundary around input matrix
input.insert(0, [-1] * len(input[0]))
input.insert(len(input), [-1] * len(input[0]))
for line in input:
    line.insert(0, -1)
    line.insert(len(line), -1)

all_flash = False
step = 0

while(not all_flash):
    step += 1

    #procedure 1
    for row in input:
        for index, val in enumerate(row):
            row[index] = val + 1 if val >=0 else val

    has_flash = True
    
    while has_flash:
        has_flash = False
        for row_i, row in enumerate(input):
            for col_i, val in enumerate(row):
                if val > 9:
                    # procedure 3
                    row[col_i] = 0
                    #procedure 2
                    total_flashes += 1
                    has_flash = True
                    update_after_flash(input, row_i, col_i)               

    #for part 2:

    all_flash = True
    for row in input:
        for val in row:
            if val > 0:
                all_flash = False
                break
        
        if not all_flash:
            break
    
    if all_flash:
        print(step)


print (total_flashes)
print(input)