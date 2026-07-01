import matplotlib.pyplot as plt

algorithms = ['BFS', 'Dijkstra', 'A*']

nodes = [40, 36, 22]

plt.figure(figsize=(6,4))

plt.bar(algorithms, nodes)

plt.title("Nodes Expanded in Maze Environment")

plt.xlabel("Algorithm")

plt.ylabel("Visited Nodes")

plt.savefig("figures/nodes_maze.png")

plt.show()