# Depth-First Search (DFS) Algorithm Implementation
# Example Graph representing a game map

def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()           # To keep track of visited nodes
    if path is None:
        path = []                 # To store the path being explored

    # Mark the current node as visited
    visited.add(start)
    path.append(start)

    print(f"Visited: {start}")    # Visualization of traversal order

    # If goal node is found
    if start == goal:
        print("Goal found! Path:", path)
        return True

    # Explore neighbors (recursively)
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited, path):
                return True

    # Backtrack if goal not found in this path
    path.pop()
    return False


# Example Graph (Game Map)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Starting node = 'A', Goal node = 'F'
dfs(graph, 'A', 'F')
