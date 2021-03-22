
from cartesian_product import cartesian_product

def two_variable_function(x, y):
        return (x-1)**2 + (y-1)**3

def grid_search(f, grid_points):
    grid = cartesian_product(grid_points)
    min_args, min_value = grid[0], f(*grid[0])
    for i in range(1, len(grid)):
        if f(*grid[i]) < min_value:
            min_args, min_value = grid[i], f(*grid[i])
    return min_args


x_lines = [0, 0.25, 0.75]
y_lines = [0.9, 1, 1.1, 1.2]
grid_points = [x_lines, y_lines]
argmin =  [0.75, 0.9]

assert( grid_search(two_variable_function, grid_points) == argmin )
