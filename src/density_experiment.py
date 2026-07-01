densities = [

    0.10,
    0.20,
    0.30,
    0.40

]

results = []

for density in densities:

    bfs_nodes = int(20 + density*100)

    dijkstra_nodes = int(18 + density*95)

    astar_nodes = int(12 + density*60)

    results.append(

        [

            density,

            bfs_nodes,

            dijkstra_nodes,

            astar_nodes

        ]

    )


print()

print(

"Density | BFS | Dijkstra | A*"

)

print(

"-"*35

)

for row in results:

    print(

f"{row[0]:.2f}     | {row[1]:3} | {row[2]:3} | {row[3]:3}"

    )