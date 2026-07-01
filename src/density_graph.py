import matplotlib.pyplot as plt


density = [

0.10,
0.20,
0.30,
0.40

]

bfs = [

30,
40,
50,
60

]

dijkstra = [

27,
37,
46,
56

]

astar = [

18,
24,
30,
36

]


plt.figure(

figsize=(7,5)

)

plt.plot(

density,

bfs,

marker='o',

label='BFS'

)

plt.plot(

density,

dijkstra,

marker='o',

label='Dijkstra'

)

plt.plot(

density,

astar,

marker='o',

label='A*'

)

plt.xlabel(

'Obstacle Density'

)

plt.ylabel(

'Visited Nodes'

)

plt.title(

'Effect of Obstacle Density'

)

plt.legend()

plt.grid()

plt.savefig(

'figures/density_graph.png'

)

plt.show()