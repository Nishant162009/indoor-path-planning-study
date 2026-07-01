from maps import *

def show(grid):

    for row in grid:
        print(" ".join(row))

    print()

print("Empty Room")
show(empty_room)

print("Office")
show(office)

print("Maze")
show(maze)

print("Warehouse")
show(warehouse)