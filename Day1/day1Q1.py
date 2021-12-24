from os import system


prev_depth = 500
result = 0
with open("Day1Q1Input.txt") as f:
    lines = f.readlines()
    for line in lines:
        current_depth = int(line.strip())
        if current_depth > prev_depth:
            result += 1
        prev_depth = current_depth
print(result)
