input = []
with open("C:\\Users\\ztang\\Desktop\\AdventCode2021\\Day10\\Day10Input.txt") as f:
    input = f.readlines()

brakets = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

score = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

score2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

result = 0
result2 = []

for line in input:
    line = line.strip()
    corrupted = False
    stack = []
    for char in line:
        if char in brakets.keys():
            stack.append(char)
        elif len(stack) != 0 and brakets[stack.pop()] != char:
            corrupted = True
            result += score[char]

    if not corrupted:
        temp = 0
        for char in reversed(stack):
            temp = temp * 5 + score2[char]
        result2.append(temp)


print(result)
result2.sort()
mid_index = int((len(result2) - 1) / 2)
print(result2[mid_index])
