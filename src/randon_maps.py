import random


def generate_map(rows, cols, density):

    grid = []

    for i in range(rows):

        row = []

        for j in range(cols):

            if random.random() < density:

                row.append("#")

            else:

                row.append(".")

        grid.append(row)

    grid[0][0] = "S"

    grid[rows-1][cols-1] = "G"

    return grid


maze = generate_map(

    10,

    10,

    0.30

)

for row in maze:

    print(

        " ".join(row)

    )