from math import floor

# To use for Part One of the problem, instead of `is_id_invalid`, easy solution 
def is_id_invalid_simple(id: int):
    id_str = str(id)
    mid_len = floor(len(id_str)/2)
    left_half = id_str[0:mid_len]
    right_half = id_str[mid_len:]
    if left_half == right_half:
        return True


def is_id_invalid_rec(id_str, pattern):
    """
    The idea is to check recursively if the rest of the ID string is identical to the expected pattern
    """
    if not id_str:  # successfully consumed entire string
        return True
    if id_str[:len(pattern)] == pattern:
        return is_id_invalid_rec(id_str[len(pattern):], pattern)
    return False

    
def is_id_invalid(id: int):
    id_str = str(id)
    
    if len(id_str) <= 1: 
        return False
        
    mid_len = floor(len(id_str)/2)
    for i in range(1, mid_len+1):
        sub_str = id_str[0:i]
        if is_id_invalid_rec(id_str, sub_str):
            print(f"  Found invalid: {id_str} (pattern {sub_str})")
            return True
    
    return False


example_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

invalid_ids = [] 
pair_ids = example_input.split(',')

for pair_id in pair_ids:
    first_id, last_id = pair_id.split('-')
    for id in range(int(first_id), int(last_id)+1):
        if is_id_invalid(id):  # for Part One, use is_id_invalid_simple
            invalid_ids.append(id)
        
print(f"\n\nTotal invalid IDs: {len(invalid_ids)}")
print(f"Sum of invalid IDs: {sum(invalid_ids)}")