rec = [0, 0, 0, 0, 0]
report_numbers = []
bitsize = 0
with open("C:\\Users\\ztang\\Desktop\\AdventCode2021\\Day3\\Day3Input.txt") as f:
    lines = f.readlines()
    bitsize = len(lines[0].strip())
    for line in lines:
        report_numbers.append(line.strip())

    index = 0
    o2_candidate = report_numbers
    co2_candidate = report_numbers

    while index < bitsize:
        o2_candidate_1 = []
        o2_candidate_0 = []
        co2_candidate_1 = []
        co2_candidate_0 = []
        o2bitCount = 0
        co2bitCount = 0

        if len(o2_candidate) > 1:
            for number in o2_candidate:
                if number[index] == '0':
                    o2_candidate_0.append(number)
                    o2bitCount -= 1
                if number[index] == '1':
                    o2_candidate_1.append(number)
                    o2bitCount += 1
            if o2bitCount < 0:
                o2_candidate = o2_candidate_0
            else:
                o2_candidate = o2_candidate_1

        if len(co2_candidate) > 1:
            for number in co2_candidate:
                if number[index] == '0':
                    co2_candidate_0.append(number)
                    co2bitCount -= 1
                if number[index] == '1':
                    co2_candidate_1.append(number)
                    co2bitCount += 1
            if co2bitCount < 0:
                co2_candidate = co2_candidate_1
            else:
                co2_candidate = co2_candidate_0

        index += 1

    print(o2_candidate[0])
    print(co2_candidate[0])
    print(int(o2_candidate[0], 2) * int(co2_candidate[0], 2))
