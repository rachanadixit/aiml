from heapq import heappop, heappush

# A* Search Algorithm for a Maze

def a_star_search(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Function to calculate Manhattan Distance (Heuristic)
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Priority Queue for nodes to explore (stores tuples: (f, g, (r, c), path))
    open_list = []
    heappush(open_list, (0 + heuristic(start, goal), 0, start, [start]))

    visited = set()

    while open_list:
        f, g, current, path = heappop(open_list)
        r, c = current

        # If goal reached, return the path
        if current == goal:
            print("Goal reached!")
            print("Shortest Path:", path)
            return path

        # Skip if already visited
        if current in visited:
            continue
        visited.add(current)

        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Check boundaries and avoid walls (1 = wall)
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                neighbor = (nr, nc)
                if neighbor not in visited:
                    new_g = g + 1  # cost for moving one step
                    new_f = new_g + heuristic(neighbor, goal)
                    heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    print("No path found.")
    return None


# 0 = open cell, 1 = wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

# Start and Goal positions
start = (0, 0)
goal = (4, 4)

# Run the A* algorithm
a_star_search(maze, start, goal)
