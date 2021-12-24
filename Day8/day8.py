def part2(signal_patterns: list, output_values:list):
    sum = 0
    for signal_pattern, output_value in zip(signal_patterns, output_values):
        digit_patterns = ["".join(sorted(x)) for x in signal_pattern.split(" ")]
        value_patterns = ["".join(sorted(x)) for x in output_value.split(" ")]
        #print (digit_patterns)
        #print(value_patterns)
        mapping = {}
        digit_4 = ""
        digit_7 = ""

        for digit_pattern in digit_patterns:
            if len(digit_pattern) == 2:
                mapping[digit_pattern] = 1
            elif len(digit_pattern) == 4:
                mapping[digit_pattern] = 4
                digit_4 = digit_pattern
            elif len(digit_pattern) == 3:
                mapping[digit_pattern] = 7
                digit_7 = digit_pattern
            elif len(digit_pattern) == 7:
                mapping[digit_pattern] = 8
        
        digit_4 = set(digit_4)
        digit_7 = set(digit_7)
        
        for digit_pattern in digit_patterns:
            # for digit 0, 6, and 9
            if len(digit_pattern) == 6:
                if len(digit_4 & set(digit_pattern)) == 4:
                    mapping[digit_pattern] = 9
                elif len(set(digit_7) & set(digit_pattern)) == 2:
                    mapping[digit_pattern] = 6
                elif len(digit_7 & set(digit_pattern)) == 3:
                    mapping[digit_pattern] = 0
            # for digit 2, 3, 5
            if len(digit_pattern) == 5:
                if len(digit_4 & set(digit_pattern)) == 2:
                    mapping[digit_pattern] = 2
                elif len(digit_7 & set(digit_pattern)) == 3:
                    mapping[digit_pattern] = 3
                elif len(digit_7 & set(digit_pattern)) == 2:
                    mapping[digit_pattern] = 5
        
        temp = mapping[value_patterns[0]] * 1000 + mapping[value_patterns[1]] * 100 + mapping[value_patterns[2]] * 10 + mapping[value_patterns[3]]
        sum += temp
                
        
    return sum


signal_patterns = []
output_values = []
with open("C:\\Users\\ztang\\Desktop\\AdventCode2021\\Day8\\Day8Input.txt") as f:
    lines = f.readlines()
    signal_patterns = [line.strip().split(" | ")[0] for line in lines]
    output_values = [line.strip().split(" | ")[1] for line in lines]


result = 0
for output_value in output_values:
    for digit in output_value.split(" "):
        if len(digit) in (2, 3, 4, 7):
            result += 1

print(result)
print(part2(signal_patterns, output_values))
