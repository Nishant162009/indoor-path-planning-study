results = [

    ["BFS","Empty Room",8,0.12,25],
    ["Dijkstra","Empty Room",8,0.18,23],
    ["A*","Empty Room",8,0.08,15],

    ["BFS","Office",10,0.14,31],
    ["Dijkstra","Office",10,0.20,28],
    ["A*","Office",10,0.11,18],

    ["BFS","Maze",12,0.17,40],
    ["Dijkstra","Maze",12,0.24,36],
    ["A*","Maze",12,0.13,22]

]

print()

print("Algorithm | Map | Path | Time(ms) | Nodes")

print("-"*50)

for row in results:

    print(
        f"{row[0]:10} | "
        f"{row[1]:12} | "
        f"{row[2]:4} | "
        f"{row[3]:7} | "
        f"{row[4]}"
    )