sample_input = """987654321111111
811111111111119
234234234234278
818181911112111"""

def find_max_sequence(line: str) -> int:
    # Example
    # line_length: 6
    # sequence_length: 3 numbers
    # Idea: loop 3 times, one for each number to pick and pick max in allowed range
    # first number can only be picked between index 0 and (line_length - sequence_length) and is the max of that range
    # second number can only be picked between index of number picked at previous loop and (line_length - sequence_length + 1) and is the max of that range
    # etc etc 
    
    sequence_length = 12
    picked_digits = []
    
    last_picked_index = 0
    
    while len(picked_digits) < sequence_length:
        range_start = last_picked_index 
        range_end = len(line) - sequence_length + len(picked_digits) 
        
        max_digit_in_range = -1
        max_digit_index = None
        
        for offset, char in enumerate(line[range_start:range_end+1]):
            digit = int(char)
            if digit > max_digit_in_range:
                max_digit_in_range = digit
                max_digit_index = range_start + offset
        
        last_picked_index = max_digit_index + 1 
        picked_digits.append(str(max_digit_in_range))
        
    return int(''.join(picked_digits))


total_max_sum = sum(
    find_max_sequence(line, sequence_length=12)
    for line in sample_input.splitlines()
)

print(f"\n\nFINAL MAX JOLTAGE SUM: max number = {total_max_sum}")
