grid_str = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def transform_str_grid_to_2D_array(grid_str):
    return [list(line) for line in grid_str.splitlines()] 
    
def print_2D_array(arr):
    for row in arr:
        print(' '.join(row))

def check_neighbours(grid, x, y):
    neighbour_count = 0
    
    N = len(grid)
    M = len(grid[0])
    
    range_x = range(max(x-1, 0), min(x+2, M))
    range_y = range(max(y-1, 0), min(y+2, N))
    
    for y2 in range_y:
        for x2 in range_x:
            if (x==x2 and y==y2):
                continue
            if grid[y2][x2] == '@' or grid[y2][x2] == 'X':
                neighbour_count += 1

    return neighbour_count < 4


grid = transform_str_grid_to_2D_array(grid_str)
N = len(grid)
M = len(grid[0])

rolls_removed = 0
iterations = 0

while True:
    print(f"At iteration #{iterations}, removed {rolls_removed} rolls so far.")
    iterations += 1
    removable_rolls = 0
    
    # First, mark all removable rolls
    for y in range(N):
        for x in range(M):
            if grid[y][x] != '.' and check_neighbours(grid, x, y):
                grid[y][x] = 'X'
                removable_rolls += 1 
    
    print(f"    removable_rolls {removable_rolls} ")

    if removable_rolls != 0:
        # Then remove all rolls
        for y in range(N):
            for x in range(M):
                if grid[y][x] == 'X':
                    grid[y][x] = '.'
                    rolls_removed += 1 
    else:
        break
    

print(rolls_removed)