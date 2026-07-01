import csv
import matplotlib.pyplot as plt

bfs=[]
dijkstra=[]
astar=[]

with open('data/batch_results.csv') as file:

    reader = csv.DictReader(file)

    for row in reader:

        bfs.append(int(row['BFS']))

        dijkstra.append(int(row['Dijkstra']))

        astar.append(int(row['Astar']))


plt.figure(figsize=(8,5))

plt.hist(

    bfs,

    bins=10,

    alpha=0.5,

    label='BFS'

)

plt.hist(

    dijkstra,

    bins=10,

    alpha=0.5,

    label='Dijkstra'

)

plt.hist(

    astar,

    bins=10,

    alpha=0.5,

    label='A*'

)

plt.xlabel(

'Expanded Nodes'

)

plt.ylabel(

'Frequency'

)

plt.title(

'Distribution of Expanded Nodes'

)

plt.legend()

plt.grid()

plt.savefig(

'figures/histogram.png'

)

plt.show()