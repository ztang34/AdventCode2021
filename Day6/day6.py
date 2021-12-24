day = 18
input = []
with open("C:\\Users\\ztang\\Desktop\\AdventCode2021\\Day6\\TestInput.txt") as f:
    line = f.readline().strip()
    input = [int(x) for x in line.split(",")]

print(input)
newborn = 0
for i in range(day):
    
    for index in range(len(input)):
        if input[index] == 0:
            input[index] = 6
            newborn += 1
        else:
            input[index] -= 1
    input = input + [8] * newborn
    newborn = 0
    #print(f"day {i}: {input}")


print(len(input))
