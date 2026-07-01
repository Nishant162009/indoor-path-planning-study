import heapq

maze = [
    ['S', '.', '.', '.'],
    ['.', 'M', 'M', '.'],
    ['.', 'M', '.', '.'],
    ['.', '.', '.', 'G']
]

costs = {
    '.':1,
    'M':2,
    'S':1,
    'G':1
}

rows = len(maze)
cols = len(maze[0])

start = (0,0)
goal = (3,3)


def heuristic(a,b):

    return abs(a[0]-b[0]) + abs(a[1]-b[1])


pq = []

heapq.heappush(pq,(0,start))

g_cost = {start:0}

parent = {}

moves = [(1,0),(-1,0),(0,1),(0,-1)]

visited = 0


while pq:

    current_f,current = heapq.heappop(pq)

    visited += 1

    if current == goal:
        break

    r,c = current

    for dr,dc in moves:

        nr = r + dr
        nc = c + dc

        if 0 <= nr < rows and 0 <= nc < cols:

            neighbor = (nr,nc)

            tentative = (
                g_cost[current]
                +
                costs[maze[nr][nc]]
            )

            if (
                neighbor not in g_cost
                or
                tentative < g_cost[neighbor]
            ):

                g_cost[neighbor] = tentative

                f = (
                    tentative
                    +
                    heuristic(
                        neighbor,
                        goal
                    )
                )

                parent[neighbor] = current

                heapq.heappush(
                    pq,
                    (
                        f,
                        neighbor
                    )
                )

path = []

node = goal

while node != start:

    path.append(node)

    node = parent[node]

path.append(start)

path.reverse()


print("Path:\n")

for p in path:

    print(p)

print()

print("Cost:",g_cost[goal])

print()

print("Visited Nodes:",visited)