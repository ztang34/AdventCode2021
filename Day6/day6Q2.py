days = 256
input = [0] * 9
with open("C:\\Users\\ztang\\Desktop\\AdventCode2021\\Day6\\Day6Input.txt") as f:
    line = f.readline().strip()
    ages = [int(x) for x in line.split(",")]
    for age in ages:
        input[age] += 1

for day in range(days):
    birth_fish = input[0]
    for age in range(1, len(input)):
        input[age - 1] = input[age]
    input[-1] = birth_fish
    input[6] += birth_fish

result = sum(input)
print(result)