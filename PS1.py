# A* Search Algorithm Implementation
# Example Graph for finding path from A to G

def aStarAlgo(start_node, stop_node):
    # Initialize open and closed sets
    open_set = set([start_node])
    closed_set = set()

    # g stores the cost from start node to current node
    g = {}
    g[start_node] = 0

    # parents stores the parent of each node
    parents = {}
    parents[start_node] = start_node

    # Loop until open set is empty
    while open_set:
        n = None

        # Find node with the lowest f(n) = g(n) + h(n)
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n is None:
            print('Path does not exist!')
            return None

        # If the goal is reached, reconstruct the path
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found:', path)
            return path

        # Check neighbors of the current node
        for (m, weight) in get_neighbors(n):
            # If neighbor not visited yet
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                # If a better path is found
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        # Move current node to closed set
        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None


# Function to return neighbors of a node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return []


# Heuristic values for each node
def heuristic(n):
    heuristic_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0
    }
    return heuristic_dist[n]

# Graph representation: each node -> list of (neighbor, cost)
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'E': [('D', 6)],
    'D': [('G', 1)],
    'G': []
}

# Run the algorithm
aStarAlgo('A', 'G')
