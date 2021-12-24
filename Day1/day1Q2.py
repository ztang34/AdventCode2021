prev_depth = 500
result = 0
depths_data = []
with open("Day1Q1Input.txt") as f:
    lines = f.readlines()
    for line in lines:
        depths_data.append(int(line.strip()))
i = 0
j = 3

while j < len(depths_data):
    if depths_data[j] > depths_data[i]:
        result += 1
    i += 1
    j += 1

print(result)
