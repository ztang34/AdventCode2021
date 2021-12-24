from string import ascii_uppercase


alphabet = {}
polymer = []
rules = {}
steps = 40

def part2():
    polymer_unit = {}
    alphabet = {}

    #initialize polymer_unit
    for unit in rules.keys():
        polymer_unit[unit] = 0
    for i in range(len(polymer) - 1):
        pair = "".join(polymer[i: i+2])
        polymer_unit[pair] += 1
    

    #loop through steps
    for _ in range(steps):
        #keep track of new polymer
        polymer_unit_new ={}
        for unit in rules.keys():
            polymer_unit_new[unit] = 0
        
        #loop through current polymer units:
        for unit, number in polymer_unit.items():
            if number > 0:
                inserted_char = rules[unit]
                new_unit_1 = unit[0] + inserted_char
                new_unit_2 = inserted_char + unit[1]
                polymer_unit_new[new_unit_1] += number
                polymer_unit_new[new_unit_2] += number
        
        polymer_unit = polymer_unit_new
    
    for char in ascii_uppercase:
        alphabet[char] = 0
    
    for unit, number in polymer_unit.items():
        alphabet[unit[0]] += number
        alphabet[unit[1]] += number
    
    alphabet[polymer[0]] += 1
    alphabet[polymer[1]] += 1
    print((max(alphabet.values())- min(i for i in alphabet.values() if i > 0))/ 2)



# read from input text
with open("C:\\Users\\ztang\\Desktop\\AdventCode2021\\Day14\\Day14Input.txt") as f:
    input = f.read().split("\n\n")
    polymer = list(input[0].strip())
    rules_raw = [x.strip().split(" -> ") for x in input[1].split("\n")]
    for rule in rules_raw:
        rules[rule[0]] = rule[1]

part2()

# initialize alphabet
for char in ascii_uppercase:
    alphabet[char] = 0

for char in polymer:
    alphabet[char] += 1

# loop through each step:
for _ in range(steps):
    added_element = []
    for i in range(len(polymer) - 1):
        pair = "".join(polymer[i: i+2])
        added_element.append(rules[pair])
        alphabet[rules[pair]] += 1

    for index, element in enumerate(added_element):
        polymer.insert(2 * index + 1, element)

print(len(polymer))
print(alphabet)
print(max(alphabet.values())- min(i for i in alphabet.values() if i > 0))






    

    

    
