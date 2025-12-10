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


def parse_command(command):
    return (command[0], int(command[1:]))

def print_msg(direction, distance, new_position, passed_zero=0):
    passed_zero_msg = ""
    if passed_zero > 0:
        word = f"{passed_zero} times"
        if passed_zero == 1:
            word = "once"
        elif passed_zero == 2:
            word = "twice"
        passed_zero_msg = f"; during this rotation, it \n  points at 0 {word}"

    print(f"- The dial is rotated {direction}{distance} to point at {new_position}{passed_zero_msg}")

number_of_zeroes = 0 
number_of_commands = 0
current_position = 50

commands = sample_commands

print(f"- The dial starts by pointing at {current_position}.")
for line in commands.splitlines():
    number_of_commands += 1
    direction, distance = parse_command(line)
    passed_zeroes = 0
    steps_left = distance
    
    while steps_left > 0:
        step = -1 if direction == 'L' else 1
        current_position = (current_position + step) % 100
        if current_position == 0:
            passed_zeroes += 1
        steps_left -= 1 
    
    number_of_zeroes += passed_zeroes
    
    print_msg(direction, distance, current_position, passed_zeroes)
    


print(f"\n\nNumber of times we clicked 0: {number_of_zeroes}")