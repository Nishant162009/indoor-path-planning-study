import csv

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

with open(
    "data/auto_results.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow(

        [
            "Algorithm",
            "Map",
            "PathLength",
            "Time",
            "Nodes"
        ]

    )

    writer.writerows(results)

print()

print(
    "Results saved successfully."
)

print()

print(
    "File created:"
)

print(
    "data/auto_results.csv"
)