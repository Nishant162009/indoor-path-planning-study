import csv


bfs = []

dijkstra = []

astar = []


with open(

'data/batch_results.csv'

) as file:


    reader = csv.DictReader(

        file

    )


    for row in reader:


        bfs.append(

            int(

                row['BFS']

            )

        )


        dijkstra.append(

            int(

                row['Dijkstra']

            )

        )


        astar.append(

            int(

                row['Astar']

            )

        )



print()

print(

"Average Nodes"

)

print(

"--------------"

)

print(

"BFS:",

round(

sum(bfs)/len(bfs),

2

)

)


print(

"Dijkstra:",

round(

sum(dijkstra)/len(dijkstra),

2

)

)


print(

"A*:",

round(

sum(astar)/len(astar),

2

)

)