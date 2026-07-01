import random

ROWS = 10
COLS = 10

OBSTACLE_PROB = 0.25


grid = []

for i in range(ROWS):

    row = []

    for j in range(COLS):

        if random.random() < OBSTACLE_PROB:

            row.append("#")

        else:

            row.append(".")

    grid.append(row)


grid[0][0] = "S"

grid[ROWS-1][COLS-1] = "G"


for row in grid:

    print(" ".join(row))