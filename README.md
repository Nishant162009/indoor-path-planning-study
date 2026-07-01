# 🤖 A Comparative Study of Path Planning Algorithms for Indoor Mobile Robots Using Simulation

## Overview

This repository presents an independent research project investigating classical path-planning algorithms for indoor robotic navigation.

The study evaluates and compares three widely used search algorithms:

* Breadth-First Search (BFS)
* Dijkstra's Algorithm
* A* Search

Through simulation-based experimentation, the project examines algorithmic performance across multiple indoor environments and randomized scenarios.

---

## Research Question

> Which path planning algorithm is most suitable for indoor mobile robots operating in structured environments?

Performance was evaluated using:

* Path Length
* Nodes Expanded
* Computational Effort
* Obstacle Density
* Statistical Consistency

---

## Experimental Environments

Simulated environments include:

✅ Empty Room

✅ Office Layout

✅ Maze Environment

✅ Warehouse Layout

✅ Randomly Generated Maps

---

## Algorithms Implemented

| Algorithm | Type              | Optimal | Heuristic |
| --------- | ----------------- | ------- | --------- |
| BFS       | Uninformed Search | Yes     | No        |
| Dijkstra  | Cost-Based Search | Yes     | No        |
| A*        | Heuristic Search  | Yes     | Yes       |

---

## Experimental Pipeline

```text
Map Generation
      ↓

Path Planning
      ↓

Benchmark Execution
      ↓

Performance Metrics
      ↓

CSV Dataset
      ↓

Statistical Analysis
      ↓

Visualization
      ↓

Research Manuscript
```

---

## Project Structure

```text
RESEARCH/

├── src/
│   ├── bfs.py
│   ├── dijkstra.py
│   ├── astar.py
│   ├── benchmark.py
│   ├── random_maps.py
│   ├── density_experiment.py
│   └── statistics.py

├── data/
│   ├── results.csv
│   ├── density_results.csv
│   └── batch_results.csv

├── figures/
│   ├── histogram.png
│   ├── boxplot.png
│   ├── nodes_maze.png
│   └── time_maze.png

├── paper/
│   ├── draft.docx
│   ├── references.txt
│   └── notes.txt

├── README.md
└── requirements.txt
```

---

## Results Summary

Average nodes expanded over 50 randomized experiments:

| Algorithm | Average Nodes |
| --------- | ------------- |
| BFS       | 44.1          |
| Dijkstra  | 39.8          |
| A*        | 25.8          |

### Key Findings

* A* consistently expanded fewer nodes.
* Dijkstra produced optimal paths but explored more states.
* BFS remained effective in smaller environments.
* Increasing obstacle density significantly affected uninformed search strategies.

---

## Statistical Analysis

The project includes:

* Histograms
* Boxplots
* Density Studies
* Batch Experiments
* Randomized Benchmarking

Generated visualizations:

* `histogram.png`
* `boxplot.png`
* `nodes_maze.png`
* `time_maze.png`

---

## Technologies Used

Python 3.12+

NumPy

Matplotlib

VS Code

Git

GitHub

---

## Research Outputs

* Simulation Framework
* Benchmark Dataset
* Statistical Visualizations
* Research Manuscript
* GitHub Repository

---

## Future Work

Potential extensions include:

* RRT
* RRT*
* Probabilistic Roadmaps (PRM)
* Dynamic Obstacles
* Continuous Space Navigation
* ROS Integration
* Webots/Gazebo Simulations

---

## Repository

Code, datasets, figures, and manuscript are available in this repository.

---

## Author

Nishant

Class 12 Independent Research Project

2026

---

*"Robotics is not only about building machines; it is also about understanding how intelligent systems make decisions in complex environments."*
