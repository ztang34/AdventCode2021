rec = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
gamma = 0
epsilong = 0
with open("Day3Input.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        i = 0
        while i < len(line):
            if line[i] == '1':
                rec[i] += 1
            else:
                rec[i] -= 1
            i += 1

index = 0
while index < len(rec):
    if rec[index] < 0:
        epsilong += 2 ** (11 - index)
    else:
        gamma += 2 ** (11 - index)
    index += 1

print(epsilong * gamma)
