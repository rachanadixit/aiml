from collections import deque

# Define movement directions: Up, Down, Left, Right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid_move(maze, visited, row, col):
    """Check if the move is valid: inside maze, not a wall, and not visited."""
    return (0 <= row < len(maze)) and (0 <= col < len(maze[0])) and \
           (maze[row][col] == 0) and (not visited[row][col])

def bfs_shortest_path(maze, start, goal):
    """
    Use Breadth-First Search (BFS) to find the shortest path in a maze.
    maze: 2D grid (0 = free cell, 1 = wall)
    start, goal: (row, col)
    """

    # Queue for BFS — stores (current_cell, path_taken)
    queue = deque([(start, [start])])

    # Create a 2D 'visited' matrix using nested loops
    visited = []
    for i in range(len(maze)):              # loop over rows
        row = []
        for j in range(len(maze[0])):       # loop over columns
            row.append(False)               # mark all cells as not visited
        visited.append(row)

    # Mark the starting cell as visited
    visited[start[0]][start[1]] = True

    # BFS Loop — explore the maze
    while queue:
        # Dequeue the front element (FIFO)
        (r, c), path = queue.popleft()

        # Check if goal is reached
        if (r, c) == goal:
            print("✅ Shortest path found:", path)
            print("📏 Number of steps:", len(path) - 1)
            return path

        # Explore all four possible directions
        for dr, dc in directions:
            new_r = r + dr
            new_c = c + dc

            # Check if the new move is valid
            if is_valid_move(maze, visited, new_r, new_c):
                visited[new_r][new_c] = True
                queue.append(((new_r, new_c), path + [(new_r, new_c)]))

    # If queue becomes empty — no path found
    print("❌ No path found!")
    return None


# ------------------------------
# Example Maze (0 = free cell, 1 = wall)
# ------------------------------
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)  # Starting cell
goal = (4, 4)   # Goal cell

# Run BFS
bfs_shortest_path(maze, start, goal)
