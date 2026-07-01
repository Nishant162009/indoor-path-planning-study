import csv
import matplotlib.pyplot as plt

bfs=[]
dijkstra=[]
astar=[]

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


plt.figure(

figsize=(7,5)

)

plt.boxplot(

[

bfs,

dijkstra,

astar

]

)

plt.xticks(

[1,2,3],

[

'BFS',

'Dijkstra',

'A*'

]

)

plt.ylabel(

'Expanded Nodes'

)

plt.title(

'Node Expansion Comparison'

)

plt.grid()

plt.savefig(

'figures/boxplot.png'

)

plt.show()