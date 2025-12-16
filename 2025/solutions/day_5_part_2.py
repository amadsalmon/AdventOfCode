ranges_str = """
3-5
10-14
16-20
12-18
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
    return merged

ranges_parsed = parse_ranges(ranges_str)
ranges_consolidated = consolidate(ranges_parsed)

counter = 0
for r in ranges_consolidated:
    counter += (r[1]-r[0]) + 1

print(f"Number of valid IDs in ranges: {counter}")

