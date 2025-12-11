sample_input = """987654321111111
811111111111119
234234234234278
818181911112111"""

sum_max = 0

for line in sample_input.splitlines():
    current_max = 0
    for _, left_number in enumerate(line):
        for _, right_number in enumerate(line[left_index+1:]):
            current_joltage = int(left_number)*10 + int(right_number)
            if  current_joltage > current_max:
                current_max = current_joltage
    print(current_max)
    sum_max += current_max
    
print(sum_max)