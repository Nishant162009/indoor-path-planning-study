from collections import deque

maze = [
    ['S', '.', '.', '.'],
    ['#', '#', '.', '#'],
    ['.', '.', '.', '.'],
    ['.', '#', '#', 'G']
]

rows = len(maze)
cols = len(maze[0])

start = (0,0)
goal = (3,3)

queue = deque([start])

visited = set()
visited.add(start)

parent = {}

moves = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:

    current = queue.popleft()

    if current == goal:
        break

    r,c = current

    for dr,dc in moves:

        nr = r + dr
        nc = c + dc

        if (
            0 <= nr < rows
            and 0 <= nc < cols
            and maze[nr][nc] != '#'
            and (nr,nc) not in visited
        ):

            visited.add((nr,nc))

            parent[(nr,nc)] = current

            queue.append((nr,nc))


path = []

node = goal

while node != start:

    path.append(node)

    node = parent[node]

path.append(start)

path.reverse()

print("Shortest Path:")

for p in path:
    print(p)

print()

print("Path Length:", len(path)-1)

display = [row[:] for row in maze]

for r, c in path:

    if display[r][c] == '.':
        display[r][c] = '*'

print()

print("Maze with path:")

for row in display:
    print(" ".join(row))