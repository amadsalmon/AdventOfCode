sample_commands = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def get_new_position(current_position, direction, distance):
    if direction == 'R':
        new_position = (current_position + distance) % 100
    else:
        new_position = (current_position- distance) % 100
    
    print(f"The dial is rotated {direction}{distance} to point at {new_position}.")
    return new_position

def parse_command(command):
    return (command[0], int(command[1:]))
        

number_of_zeroes = 0 
number_of_commands = 0
current_position = 50

for line in sample_commands.splitlines():
    number_of_commands += 1
    direction, distance = parse_command(line)
    current_position = get_new_position(current_position, direction, distance)
    if current_position == 0:
        number_of_zeroes += 1
    
    
print(f"number_of_commands: {number_of_commands}")
print(f"number_of_zeroes: {number_of_zeroes}")
