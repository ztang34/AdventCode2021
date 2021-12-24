x = 0
y = 0
aim = 0
with open("Day2Q1Input.txt") as f:
    lines = f.readlines()
    for line in lines:
        command = line.split()
        if command[0] == "forward":
            x += int(command[1])
            y += aim * int(command[1])
        elif command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])

print(x * y)
