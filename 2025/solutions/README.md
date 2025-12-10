# Advent of Code 2025

See [the official page](https://adventofcode.com/2025).

---

## Day 1: Secret Entrance ⏲

See [full puzzle](https://adventofcode.com/2025/day/1).

The puzzle involves a safe with a circular dial numbered 0–99, starting at 50. A list of rotations tells you how to turn it: each rotation has a direction (L for left, R for right) and a distance (number of clicks). The dial wraps around, so moving left from 0 goes to 99, and moving right from 99 goes to 0.

**Example input:**

```
L68
L30
R48
L5
```

### Part 1
Count how many times the dial ends up pointing at 0 after completing each rotation.

### Part 2
Count how many times the dial points at 0 during any rotation, not just at the end.

---

## Day 2: Gift Shop 🎁

See [full puzzle](https://adventofcode.com/2025/day/2).

Example input:

```
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
```

### Walkthrough

#### Part One

We start easy: the first step is to separate each pair ID from each other: `pair_ids = example_input.split(',')`.

Then we separate each ID per pair: 
```python
for pair_id in pair_ids:
    first_id, second_id = pair_id.split('-')
```

Now the complexity comes, as we need to detect repeated character sequences. How to detect them? 

I'm thinking about splitting the ID in half and just check if both halves are identical. (e.g. `1188511885` -> `11885` and `11885` are equal)  
However what happens for IDs which have an odd length (e.g. 222)? I'm assuming these are automatically discarded, they're valid IDs.

Brute force solution by looping in each number in the range:

```python
for id in range(first_id, second_id):
    left_half = id[0:len(id)-1]
    right_half = id[len(id):]
    if left_half == right_half:
        return True
```

#### Part Two

Now the complexity comes from the fact that the repeating sequence can have any length, and it can be repeated multiple times. The previous solution where we cut the string in two and check the resulting two halves won't work here.  

The first thing that comes to mind to solve this problem is to:

1. Take all possible patterns from the originial string (e.g. from string '123123', we can only consider patterns '1', '12', '123'). 
    - _Note:_ we understand from this example that we need to pick patterns corresponding to slices of the first characters of the word. up to the middle of the word. A pattern that's longer than the half of the length of the word cannot be repeated, by definition.

2. Check if that pattern is repeated all along the following slices of the string. -> because pattern length is variable, a recursive solution is what comes to mind.
    - I need to figure out the recursion stopping conditions. 