from heapq import heappush, heappop

# Function to print puzzle board
def show(board):
    for i in range(0, 9, 3):
        print(board[i], board[i+1], board[i+2])
    print()

# Heuristic function (Manhattan Distance)
def h(curr, goal):
    dist = 0
    for n in range(1, 9):  # Ignore 0 (empty tile)
        x1, y1 = divmod(curr.index(n), 3)
        x2, y2 = divmod(goal.index(n), 3)
        dist += abs(x1 - x2) + abs(y1 - y2)
    return dist

# Get all possible next moves
def next_states(state):
    res = []
    zero = state.index(0)
    x, y = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            ni = nx * 3 + ny
            new = list(state)
            new[zero], new[ni] = new[ni], new[zero]
            res.append(tuple(new))
    return res

# A* Algorithm
def solve(start, goal):
    pq = []
    heappush(pq, (h(start, goal), 0, start, [start]))  # (f, g, state, path)
    seen = set()

    while pq:
        f, g, curr, path = heappop(pq)
        if curr in seen:
            continue
        seen.add(curr)

        if curr == goal:
            return path

        for nxt in next_states(curr):
            if nxt not in seen:
                g2 = g + 1
                f2 = g2 + h(nxt, goal)
                heappush(pq, (f2, g2, nxt, path + [nxt]))
    return None

# Main
if __name__ == "__main__":
    print("🧩 Simple 8-Puzzle Solver using A* Algorithm")
    print("Use 0 for the empty space.\n")

    start = tuple(map(int, input("Enter START state (9 numbers separated by space): ").split()))
    goal = tuple(map(int, input("Enter GOAL state (9 numbers separated by space): ").split()))

    print("\nSolving...\n")
    path = solve(start, goal)

    if path:
        print(f"Solved in {len(path) - 1} moves!\n")
        for step in path:
            show(step)
    else:
        print("No solution found for the given puzzle.")
