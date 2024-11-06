import numpy as np
import random
import time
import os

WIDTH, HEIGHT = 50,50

SUSCEPTIBLE = 0
INFECTED = 1
RECOVERED = 2

infection_probability = 0.3
recovery_time = 3

grid = np.zeros((WIDTH, HEIGHT), dtype=int)
infection_durations = np.zeros((WIDTH, HEIGHT), dtype=int)


def initialize_population(infection_chance=0.05):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if random.random() < infection_chance:
                grid[x, y] = INFECTED
                infection_durations[x, y] = recovery_time


def update_population():
    new_grid = grid.copy()
    new_durations = infection_durations.copy()

    for x in range(1, WIDTH - 1):
        for y in range(1, HEIGHT - 1):
            if grid[x, y] == SUSCEPTIBLE:
                neighbors = [grid[x - 1, y], grid[x + 1, y], grid[x, y - 1], grid[x, y + 1]]
                if INFECTED in neighbors and random.random() < infection_probability:
                    new_grid[x, y] = INFECTED
                    new_durations[x, y] = recovery_time

            elif grid[x, y] == INFECTED:
                new_durations[x, y] -= 1
                if new_durations[x, y] <= 0:
                    new_grid[x, y] = RECOVERED

    return new_grid, new_durations


def print_population():
    symbols = {SUSCEPTIBLE: '.', INFECTED: 'I', RECOVERED: 'R'}
    for y in range(1, HEIGHT - 1):
        row = ''.join(symbols[grid[x, y]] for x in range(1, WIDTH-1))
        print(row)
    print("\n" + "=" * WIDTH)


initialize_population(infection_chance=0.1)
steps = 20
for _ in range(steps):
    print_population()
    grid, infection_durations = update_population()
    time.sleep(0.5)
    os.system("clear")
