input = []
with open("C:\\Users\\ztang\\Desktop\\AdventCode2021\\Day7\\Day7Input.txt") as f:
    input = [int(x) for x in f.readline().strip().split(",")]

fuel = -1

for target in range(min(input), max(input) + 1):
    temp = 0
    for pos in input:
        temp += (1 + abs(target - pos)) * abs (target- pos) / 2
    
    if (fuel < 0) or (temp < fuel):
        fuel = temp

print(fuel)

