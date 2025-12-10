# Advent of Code 2025

See [the official page](https://adventofcode.com/2025).

## Day 1: Secret Entrance

The puzzle involves a safe with a circular dial numbered 0–99. The dial starts at 50, and a list of rotations tells you how to turn it: each rotation has a direction (L for left, R for right) and a distance (number of clicks). The dial wraps around, so moving left from 0 goes to 99, and moving right from 99 goes to 0.

For example, suppose the attached document contained the following rotations:

```
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
```

### Part 1:

**Count how many times the dial ends up pointing at 0 after completing each rotation.**

Following these rotations would cause the dial to move as follows:

```
The dial starts by pointing at 50.
The dial is rotated L68 to point at 82.
The dial is rotated L30 to point at 52.
The dial is rotated R48 to point at 0.
The dial is rotated L5 to point at 95.
The dial is rotated R60 to point at 55.
The dial is rotated L55 to point at 0.
The dial is rotated L1 to point at 99.
The dial is rotated L99 to point at 0.
The dial is rotated R14 to point at 14.
The dial is rotated L82 to point at 32.
```

Because the dial points at 0 a total of three times during this process, the password in this example is 3.

### Part 2:

**Count how many times the dial points at 0 during any rotation, not just at the end.**

Following the same rotations as in the above example, the dial points at zero a few extra times during its rotations:

```
The dial starts by pointing at 50.
The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
The dial is rotated L30 to point at 52.
The dial is rotated R48 to point at 0.
The dial is rotated L5 to point at 95.
The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
The dial is rotated L55 to point at 0.
The dial is rotated L1 to point at 99.
The dial is rotated L99 to point at 0.
The dial is rotated R14 to point at 14.
The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.
```

In this example, the dial points at 0 three times at the end of a rotation, plus three more times during a rotation. So, in this example, the new password would be 6.

