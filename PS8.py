from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    queue = deque([(0, 0, [], "Start")])  # (jug1, jug2, path, action)
    visited = set([(0, 0)])

    while queue:
        jug1, jug2, path, action = queue.popleft()
        path = path + [(action, (jug1, jug2))]

        # If target reached
        if jug1 == target or jug2 == target:
            return path

        next_moves = []

        # Fill Jug1
        next_moves.append((jug1_capacity, jug2, "Fill Jug1"))

        # Fill Jug2
        next_moves.append((jug1, jug2_capacity, "Fill Jug2"))

        # Empty Jug1
        next_moves.append((0, jug2, "Empty Jug1"))

        # Empty Jug2
        next_moves.append((jug1, 0, "Empty Jug2"))

        # Pour Jug1 → Jug2
        pour = min(jug1, jug2_capacity - jug2)
        next_moves.append((jug1 - pour, jug2 + pour, "Pour Jug1 → Jug2"))

        # Pour Jug2 → Jug1
        pour = min(jug2, jug1_capacity - jug1)
        next_moves.append((jug1 + pour, jug2 - pour, "Pour Jug2 → Jug1"))

        # Explore next states
        for next_jug1, next_jug2, act in next_moves:
            if (next_jug1, next_jug2) not in visited:
                visited.add((next_jug1, next_jug2))
                queue.append((next_jug1, next_jug2, path, act))

    return None


# --- Take input from user ---
jug1_cap = int(input("Enter capacity of Jug 1: "))
jug2_cap = int(input("Enter capacity of Jug 2: "))
target_amount = int(input("Enter target amount: "))

# --- Solve ---
solution_path = water_jug_problem(jug1_cap, jug2_cap, target_amount)

# --- Display result ---
if solution_path:
    print(f"\n✅ Solution to measure {target_amount} liters using jugs of {jug1_cap} and {jug2_cap} liters:\n")
    for i, (action, (j1, j2)) in enumerate(solution_path):
        print(f"Step {i}: {action:20s} --> (Jug1 = {j1}, Jug2 = {j2})")
    print(f"\nTotal steps: {len(solution_path) - 1}")
else:
    print(f"\n❌ No solution found for target {target_amount}.")
