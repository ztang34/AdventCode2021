from node import Node

input = []
flat_list_read_pointer = 0

with open("C:\\Users\\ztang\\Desktop\\AdventCode2021\\Day18\\Day18Input.txt") as f:
    input = [x.strip() for x in f.readlines()]


def parse_num_string_to_flat_list(num_string: str):
    layer_count = 0
    numerical_string_buffer = ""
    flat_list = []

    for c in num_string:
        if c == "[":
            if numerical_string_buffer != "":
                flat_list.append([int(numerical_string_buffer), layer_count])
                numerical_string_buffer = ""
            layer_count += 1
        elif c == "]":
            if numerical_string_buffer != "":
                flat_list.append([int(numerical_string_buffer), layer_count])
                numerical_string_buffer = ""
            layer_count -= 1
        elif c == ",":
            if numerical_string_buffer != "":
                flat_list.append([int(numerical_string_buffer), layer_count])
                numerical_string_buffer = ""
        else:
            numerical_string_buffer += c

    return flat_list


def flat_list_addition(flat_list_1, flat_list_2):
    for i in range(len(flat_list_1)):
        flat_list_1[i][1] += 1

    for i in range(len(flat_list_2)):
        flat_list_2[i][1] += 1

    return flat_list_1 + flat_list_2


def explode(input_flat_list):
    output_flat_list = []

    read_ptr = 0

    while read_ptr < len(input_flat_list):
        entry = input_flat_list[read_ptr]
        layer_count = entry[1]

        if layer_count < 5:
            output_flat_list.append(entry)
        else:
            left_value = entry[0]
            right_value = input_flat_list[read_ptr + 1][0]

            if len(output_flat_list) > 0:
                output_flat_list[-1][0] += left_value

            if read_ptr + 2 < len(input_flat_list):
                input_flat_list[read_ptr + 2][0] += right_value

            output_flat_list.append([0, layer_count - 1])

            read_ptr += 1

        read_ptr += 1

    return output_flat_list


def split(input_flat_list):
    input_flat_list = explode(input_flat_list)
    output_flat_list = []

    found_ten_digit_number = False

    for entry in input_flat_list:
        value = entry[0]
        layer_count = entry[1]

        if value >= 10 and not found_ten_digit_number:
            output_flat_list.append([value//2, layer_count + 1])
            output_flat_list.append([-(value//-2), layer_count + 1])
            found_ten_digit_number = True
        else:
            output_flat_list.append(entry)

    if found_ten_digit_number:
        return split(output_flat_list)
    else:
        return output_flat_list


def reduce(input_flat_list):
    output_flat_list = explode(input_flat_list)
    return split(output_flat_list)


def create_node(layer_count, input_flat_list):
    global flat_list_read_pointer
    node_value = input_flat_list[flat_list_read_pointer][0]
    node_layer_count = input_flat_list[flat_list_read_pointer][1]

    if node_layer_count == layer_count:
        new_node = Node(value=node_value,
                        layer=node_layer_count, is_leaf_node=True)
        flat_list_read_pointer += 1
        return new_node
    else:
        new_node = Node(layer=layer_count)
        new_node.left_child = create_node(layer_count + 1, input_flat_list)
        new_node.right_child = create_node(layer_count + 1, input_flat_list)
        return new_node


def convert_flat_list_to_binary_tree(input_flat_list):
    global flat_list_read_pointer
    flat_list_read_pointer = 0
    return create_node(0, input_flat_list)


def part2(input, results: list):
    for i in range(len(input)):
        for j in range(len(input)):
            if i != j:
                flat_list = flat_list_addition(parse_num_string_to_flat_list(
                    input[i]), parse_num_string_to_flat_list(input[j]))
                flat_list = reduce(flat_list)
                root = convert_flat_list_to_binary_tree(flat_list)
                results.append(root.get_node_value())

    return max(results)


flat_list = parse_num_string_to_flat_list(input[0])

for number in range(1, len(input)):
    flat_list = flat_list_addition(
        flat_list, parse_num_string_to_flat_list(input[number]))
    flat_list = reduce(flat_list)

root = convert_flat_list_to_binary_tree(flat_list)
print(root.get_node_value())

print(part2(input, []))
