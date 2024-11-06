import numpy as np
import time
import os

GRID_SIZE = 40
ALIVE = 1
DEAD = 0

ALIVE_SYMBOL = '0'
DEAD_SYMBOL = ' '

def initialize_grid(size):
    return np.random.choice([ALIVE, DEAD], size=(size, size))

def update_grid(grid):
    new_grid = grid.copy()

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            total = (
                grid[row, (col - 1) % GRID_SIZE]
                + grid[row, (col + 1) % GRID_SIZE]
                + grid[(row - 1) % GRID_SIZE, col]
                + grid[(row + 1) % GRID_SIZE, col]
                + grid[(row - 1) % GRID_SIZE, (col - 1) % GRID_SIZE]
                + grid[(row - 1) % GRID_SIZE, (col + 1) % GRID_SIZE]
                + grid[(row + 1) % GRID_SIZE, (col - 1) % GRID_SIZE]
                + grid[(row + 1) % GRID_SIZE, (col + 1) % GRID_SIZE]
            )

            if grid[row, col] == ALIVE:
                if total < 2 or total > 3:
                    new_grid[row, col] = DEAD
            else:
                if total == 3:
                    new_grid[row, col] = ALIVE

    return new_grid

def display_grid(grid):
    os.system('clear' if os.name == 'posix' else 'cls')
    for row in grid:
        print("".join([ALIVE_SYMBOL if cell == ALIVE else DEAD_SYMBOL for cell in row]))

def main():
    grid = initialize_grid(GRID_SIZE)

    while True:
        display_grid(grid)
        grid = update_grid(grid)
        time.sleep(0.05)

if __name__ == "__main__":
    main()
