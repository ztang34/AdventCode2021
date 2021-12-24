start = []
end = []
rec = {}

with open("C:\\Users\\ztang\\Desktop\\AdventCode2021\\Day5\\Day5Input.txt") as f:
    lines = f.readlines()
    for line in lines:
        coordinates = line.strip().split(" -> ")
        start_coordinate = coordinates[0]
        end_coordinate = coordinates[1]
        start.append(tuple(int(num) for num in start_coordinate.split(",")))
        end.append(tuple(int(num) for num in end_coordinate.split(",")))

for i in range(len(start)):
    start_x = start[i][0]
    start_y = start[i][1]
    end_x = end[i][0]
    end_y = end[i][1]

    key = ()
    if start_x == end_x:
        y_range = range(min(start_y, end_y), max(start_y, end_y)+1)
        for y in y_range:
            key = (start_x, y)
            if key in rec:
                rec[key] += 1
            else:
                rec[key] = 1
    elif start_y == end_y:
        x_range = range(min(start_x, end_x), max(start_x, end_x)+1)
        for x in x_range:
            key = (x, start_y)
            # print(key)
            if key in rec:
                rec[key] += 1
            else:
                rec[key] = 1
    elif abs(start_x - end_x) == abs(start_y - end_y):
        x_range = range(start_x, end_x, int((end_x-start_x)/abs(end_x-start_x)))
        y_range = range(start_y, end_y, int((end_y-start_y)/abs(end_y-start_y)))
        for x ,y in zip(x_range , y_range):
            key = (x,y)
            if key in rec:
                rec[key] += 1
            else:
                rec[key] = 1
        key = (end_x, end_y)
        if key in rec:
            rec[key] += 1
        else:
            rec[key] = 1


result = 0
for value in rec.values():
    if value >= 2:
        result += 1
print(result)
