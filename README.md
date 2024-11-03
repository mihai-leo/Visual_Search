This project visualizes pathfinding algorithms using Pygame,
allowing users to explore how different algorithms find a path between a starting point and an endpoint in a grid.
Each cell in the grid is assigned a random cost, simulating real-world variable movement costs.

Features
  Interactive Grid Setup: Set a start point, end point, and barriers within the grid.
  Algorithm Selection: Choose among several pathfinding algorithms, each with unique visualizations.
  Popup Info Screen: Display keyboard shortcuts and information on controls.

Supported Algorithms
  Breadth-First Search (BFS): Finds the shortest path in terms of edges traversed.
  Depth-First Search (DFS): Explores nodes in depth-first order without prioritizing the shortest path.
  A Search*: Heuristic-driven algorithm that balances exploration and path length.
  Uniform Cost Search (UCS): Prioritizes lower-cost paths and accounts for cell costs.
  Dijkstra's Algorithm: Guarantees the shortest path based on cumulative costs.
  
Controls
  SPACE: Open information window with controls and algorithm descriptions.
  R: Reset the grid with a new matrix.
  C: Clear the grid to default settings, retaining existing numbers.
  B: Execute Breadth-First Search.
  D: Execute Depth-First Search.
  A: Execute A* Search.
  U: Execute Uniform Cost Search.
  J: Execute Dijkstra's Algorithm.

  
Code Overview
1. Spot Class
Represents each cell in the grid. Contains:
  Position and Color: Coordinates and visual state (start, end, barrier, open, closed).
  Neighbors: Adjacent cells, excluding barriers.
  Draw Method: Visualizes the cell on the Pygame window.
  Cost Number: Randomized value, affecting algorithms that consider cell costs.

2. Pathfinding Algorithms
Each algorithm follows a specific logic to search for the path:
  Depth-First Search (dfs): Recursively explores paths in depth-first order.
  Breadth-First Search (bfs): Uses a queue to explore paths in breadth-first order.
  Uniform Cost Search (ucs): Uses a priority queue and considers cell costs.
  Dijkstra's Algorithm (dij): Similar to UCS but ensures optimal path.
  *A Search (a_star)**: Combines cost and heuristic for an efficient path.
   
4. Utility Functions
Grid Management:
  make_grid: Initializes a grid of cells.
  copy_grid: Copies an existing grid for visualization persistence.
  remake_grid: Resets grid for a fresh algorithm run.
Display:
  draw: Draws all cells and grid lines.
  show_popup: Displays the control instructions on a semi-transparent overlay.

Sources:
https://www.youtube.com/watch?v=JtiK0DOeI4A
