import numpy as np
import time
import os

WASSER = 0
WIESE = 1
WALD = 2
BRENNEND = 3
ABGEBRANNT = 4

SYMBOLS = {
    WASSER: '🌊',     # Wasser
    WIESE: '🌿',      # Wiese
    WALD: '🌲',       # Wald
    BRENNEND: '🔥',   # Brennend
    ABGEBRANNT: '⬛'  # Abgebrannt
}

GRID_SIZE = 50

WIESE_BRENNDAUER = 4

def initialize_grid(size):
    return np.random.choice([WASSER, WIESE, WALD], size=(size, size))

def spread_fire(grid, fire_time):
    new_grid = grid.copy()

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == BRENNEND:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    n_row, n_col = (row + dx) % GRID_SIZE, (col + dy) % GRID_SIZE
                    if grid[n_row, n_col] == WALD:
                        new_grid[n_row, n_col] = BRENNEND
                    elif grid[n_row, n_col] == WIESE and fire_time[n_row, n_col] == 0:
                        new_grid[n_row, n_col] = BRENNEND
                        fire_time[n_row, n_col] = WIESE_BRENNDAUER

                new_grid[row, col] = ABGEBRANNT
            elif grid[row, col] == BRENNEND and fire_time[row, col] > 0:
                fire_time[row, col] -= 1
                if fire_time[row, col] == 0:
                    new_grid[row, col] = ABGEBRANNT

    return new_grid

def display_grid(grid):
    os.system('clear' if os.name == 'posix' else 'cls')
    for row in grid:
        print("".join([SYMBOLS[cell] for cell in row]))

def main():
    grid = initialize_grid(GRID_SIZE)
    fire_time = np.zeros_like(grid)

    num_fires = 3
    fire_positions = np.random.choice(GRID_SIZE * GRID_SIZE, num_fires, replace=False)
    for pos in fire_positions:
        row, col = divmod(pos, GRID_SIZE)
        if grid[row, col] != WASSER:
            grid[row, col] = BRENNEND

    while True:
        display_grid(grid)
        grid = spread_fire(grid, fire_time)
        time.sleep(0.1)

        if BRENNEND not in grid:
            break

if __name__ == "__main__":
    main()
