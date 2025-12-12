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
    

valid_rolls = 0

grid_copy = grid

for y in range(N):
    for x in range(M):
        if grid_copy[y][x] != '.' and check_neighbours(grid,x,y):
            grid_copy[y][x] = 'X'
            valid_rolls += 1 

print(valid_rolls)