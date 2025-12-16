ranges_str = """
3-5
10-14
16-20
12-18
"""

ids_str = """
1
5
8
6
23
15
"""


def parse_ranges(s: str):
    return [
        tuple(map(int, line.split("-")))
        for line in s.strip().splitlines()
    ]
    
def consolidate(ranges):
    ranges = sorted(ranges)
    merged = []

    for start, end in ranges:
        if not merged or start > merged[-1][1]:
            merged.append((start, end))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    print(f"Before consolidation: {len(ranges)} ranges. \nAfter consolidation: {len(merged)} ranges.")
    return merged


def is_id_in_ranges(id, ranges):
    if not ranges:
        return False

    mid_range_idx = int(len(ranges) / 2)
    mid_range = ranges[mid_range_idx]
    range_start = mid_range[0]
    range_end = mid_range[1]
    
    if id < range_start:
        return is_id_in_ranges(id, ranges[0:mid_range_idx])
    elif id > range_end:
        return is_id_in_ranges(id, ranges[mid_range_idx+1:])
    else:
        return True


ranges_parsed = parse_ranges(ranges_str)
ranges_consolidated = consolidate(ranges_parsed)

counter = 0
for i in ids_str.splitlines():
    counter += 1 if is_id_in_ranges(int(i), ranges_consolidated) else 0

print(f"\nNumber of IDs in valid ranges: {counter}")
