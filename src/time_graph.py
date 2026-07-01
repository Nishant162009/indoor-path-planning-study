import matplotlib.pyplot as plt

algorithms = ['BFS', 'Dijkstra', 'A*']

times = [0.17, 0.24, 0.13]

plt.figure(figsize=(6,4))

plt.bar(algorithms, times)

plt.title("Execution Time in Maze")

plt.xlabel("Algorithm")

plt.ylabel("Time (ms)")

plt.savefig("figures/time_maze.png")

plt.show()