import heapq

maze = [
    ['S', '.', '.', '.'],
    ['.', 'M', 'M', '.'],
    ['.', 'M', '.', '.'],
    ['.', '.', '.', 'G']
]

costs = {
    '.': 1,
    'M': 5,
    'S': 1,
    'G': 1
}

rows = len(maze)
cols = len(maze[0])

start = (0,0)
goal = (3,3)

pq = []

heapq.heappush(pq, (0, start))

distance = {}

distance[start] = 0

parent = {}

moves = [(1,0),(-1,0),(0,1),(0,-1)]

while pq:

    current_cost, current = heapq.heappop(pq)

    if current == goal:
        break

    r,c = current

    for dr,dc in moves:

        nr = r + dr
        nc = c + dc

        if 0 <= nr < rows and 0 <= nc < cols:

            new_cost = current_cost + costs[maze[nr][nc]]

            if (nr,nc) not in distance or new_cost < distance[(nr,nc)]:

                distance[(nr,nc)] = new_cost

                parent[(nr,nc)] = current

                heapq.heappush(
                    pq,
                    (new_cost, (nr,nc))
                )

path = []

node = goal

while node != start:

    path.append(node)

    node = parent[node]

path.append(start)

path.reverse()

print("Path:")

for p in path:
    print(p)

print()

print("Total Cost:")
print(distance[goal])