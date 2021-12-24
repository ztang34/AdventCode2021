from math import prod

input = str()
versions = []


def parse_packet(packet, read_ptr):
    #read version

    versions.append(int(packet[read_ptr: read_ptr + 3], 2))
    read_ptr += 3

    #read type
    data_type = int(packet[read_ptr : read_ptr + 3], 2)
    read_ptr += 3

    # if the data type is liberal value
    if data_type == 4:
        chunks = []
        continue_read = "1"

        while continue_read == "1":
            chunk = packet[read_ptr : read_ptr + 5]
            continue_read = chunk[0]
            chunks.append(chunk[1:5])
            read_ptr += 5
        
        return (int("".join(chunks), 2), read_ptr)
    
    else:
        values = []
        length_type = packet[read_ptr]
        read_ptr += 1

        if length_type == "0":
            total_length = int(packet[read_ptr : read_ptr + 15], 2)
            read_ptr += 15
            target_read_ptr = read_ptr + total_length

            while read_ptr < target_read_ptr:
                (value, read_ptr) = parse_packet(packet, read_ptr)
                values.append(value)
        
        else:
            total_sub_packets = int(packet[read_ptr : read_ptr + 11], 2)
            read_ptr += 11
            
            for _ in range(total_sub_packets):
                (value, read_ptr) = parse_packet(packet, read_ptr)
                values.append(value)
        
        result = 0
        if data_type == 0:
            result = sum(values)
        elif data_type == 1:
            result = prod(values)
        elif data_type == 2:
            result = min(values)
        elif data_type == 3:
            result = max(values)
        elif data_type == 5:
            result = int(values[0] > values[1])
        elif data_type == 6:
            result = int(values[0] < values[1])
        elif data_type == 7:
            result = int(values[0] == values[1])
        

        return (result, read_ptr)






with open("C:\\Users\\ztang\\Desktop\\AdventCode2021\\Day16\\Day16Input.txt") as f:
    raw_hex = f.readline()
    num_of_bits = len(raw_hex) * 4
    input = bin(int(raw_hex, 16))[2:].zfill(num_of_bits)
    (value, ptr) = parse_packet(input, 0)
    print(value)
    print(ptr)
    print(sum(versions))


